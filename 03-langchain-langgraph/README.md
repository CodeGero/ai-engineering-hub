# 03 — Production Agents with LangGraph

Tutorial 02 built the agent loop by hand. In production you want:
**state management, branching, retries, human approval, and persistence.** That's
what LangGraph gives you — you describe the agent as a **graph** of nodes.

- LangChain: 141k★ · LangGraph: 37k★. The dominant production stack.

## Install
```bash
pip install langgraph langchain-openai
export OPENAI_API_KEY=sk-...   # or swap for a local model via Ollama
```

## A minimal stateful agent
```python
from typing import TypedDict, Annotated
import operator
from langgraph.graph import StateGraph, END

class State(TypedDict):
    input: str
    messages: Annotated[list, operator.add]
    output: str

def call_model(s: State):
    # replace with real LLM call
    reply = f"[model] responding to: {s['input']}"
    return {"messages": [reply], "output": reply}

def should_continue(s: State):
    # branch: stop after one reply for this demo
    return END

builder = StateGraph(State)
builder.add_node("model", call_model)
builder.set_entry_point("model")
builder.add_conditional_edges("model", should_continue)
graph = builder.compile()

result = graph.invoke({"input": "Hello"})
print(result["output"])
```

## Why graphs?
- **Explicit control flow.** Loops, forks, and joins are visible, not hidden in recursion.
- **Persistence.** LangGraph can save state to Postgres so an agent resumes after a crash.
- **Human-in-the-loop.** Insert an `approve` node that pauses for a person.

## When NOT to use it
For a one-shot script, Tutorial 02's 80 lines are simpler. Reach for LangGraph when
you have **multiple steps, need to recover from failure, or must persist state.**

→ Next: [04 Multi-Agent with AutoGen](04-multi-agent-autogen/README.md)
