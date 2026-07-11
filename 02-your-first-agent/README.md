# 02 — Build Your First Agent (From Scratch, Zero Frameworks)

Frameworks are great. But if you don't understand the loop, you can't debug them.
Here we build a working agent in ~80 lines of plain Python that:

- talks to a local model (Ollama — free, private),
- calls **tools** (a calculator and a "current time" function),
- loops: think → act → observe → repeat, until it answers.

No LangChain. No AutoGen. Just the core idea.

---

## 1. Install Ollama and a model

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh
# Windows: download from https://ollama.com/download

ollama pull llama3.2      # ~2GB, runs on most laptops
```

Test it:
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{"role":"user","content":"say hi in 3 words"}]
}'
```

If you get JSON back, Ollama is running. That's your agent's "brain."

---

## 2. The agent code

Save as `agent.py`:

```python
import json, urllib.request
from datetime import datetime

OLLAMA = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

# ---- Tools -------------------------------------------------------------
def calc(expr: str) -> str:
    """Evaluate a basic arithmetic expression safely (no eval())."""
    try:
        # allow only digits and operators
        import re
        if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
            return "error: only numbers and + - * / ( ) allowed"
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"error: {e}"

def now(_: str = "") -> str:
    """Return the current UTC time."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

TOOLS = {
    "calc": {"fn": calc, "desc": "Evaluate arithmetic, e.g. calc('2*(3+4)')."},
    "now":  {"fn": now,  "desc": "Get current UTC time. Call as now('')."},
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
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["message"]["content"]

def run(user_task: str, max_steps: int = 5):
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
            if not tool:
                obs = f"error: unknown tool {name}"
            else:
                obs = tool["fn"](arg)
            print(f"           tool {name}({arg!r}) -> {obs}")
            messages.append({"role": "assistant", "content": out})
            messages.append({"role": "user", "content": f"Observation: {obs}. Continue."})
    return "(max steps reached)"

if __name__ == "__main__":
    print(run("What is 17 times the current hour UTC? Show your work via tools."))
```

Run it:
```bash
python agent.py
```

You'll see the loop think, call `now()`, call `calc()`, and produce an `ANSWER:`.

---

## 3. Why this is an "agent"

The model doesn't compute 17×hour itself. It **decides** to call `now()`, then
**decides** to call `calc()` with the observed value, then **decides** it has
enough to answer. That decide → act → observe loop *is* agency.

Everything else in the ecosystem (LangGraph, AutoGen, CrewAI) is elaboration of
this loop: better state, more tools, multiple agents, retries, memory. Once you
can write this in 80 lines, those frameworks become comprehensible instead of
mysterious.

---

## 4. Exercise
Add a third tool: `web(title)` that searches your local notes (a dict). Then ask
the agent a question that requires it. Watch it chain all three tools.

→ Next: [03 Production Agents with LangGraph](03-langchain-langgraph/README.md)
