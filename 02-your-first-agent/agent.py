"""Tutorial 02 — a minimal ReAct agent (no frameworks).

Requires Ollama running locally with `ollama pull llama3.2`.
  pip not needed; uses only stdlib + Ollama's HTTP API.

Run:  python agent.py
"""
import json
import re
import urllib.request
from datetime import datetime, timezone

OLLAMA = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


# ---- Tools -------------------------------------------------------------
def calc(expr: str) -> str:
    """Evaluate basic arithmetic safely (no eval of arbitrary code)."""
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
        return "error: only numbers and + - * / ( ) allowed"
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:  # noqa: BLE001
        return f"error: {e}"


def now(_: str = "") -> str:
    """Return current UTC time."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


TOOLS = {
    "calc": calc,
    "now": now,
}

SYSTEM = """You are a tool-using agent. To use a tool, reply with EXACTLY:
ACTION: <tool_name>(<argument>)
When you have the final answer, reply with:
ANSWER: <your answer>
Available tools: calc(expr), now('')."""


def ask(messages):
    body = json.dumps({"model": MODEL, "messages": messages,
                       "stream": False}).encode()
    req = urllib.request.Request(OLLAMA, data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["message"]["content"]


def run(user_task: str, max_steps: int = 5) -> str:
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_task}]
    for step in range(max_steps):
        out = ask(messages).strip()
        print(f"[step {step}] model: {out}")
        if out.startswith("ANSWER:"):
            return out[len("ANSWER:"):].strip()
        if out.startswith("ACTION:"):
            call = out[len("ACTION:"):].strip()
            name, arg = call.split("(", 1)
            arg = arg.rstrip(")").strip().strip("'\"")
            tool = TOOLS.get(name)
            obs = f"error: unknown tool {name}" if not tool else tool(arg)
            print(f"           tool {name}({arg!r}) -> {obs}")
            messages.append({"role": "assistant", "content": out})
            messages.append({"role": "user",
                             "content": f"Observation: {obs}. Continue."})
    return "(max steps reached)"


if __name__ == "__main__":
    print(run("What is 17 times the current hour UTC? Use your tools."))
