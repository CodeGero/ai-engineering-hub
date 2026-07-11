# 00 — Start Here

Welcome. This repo teaches you to **build with AI agents**, not just use chatbots.

## Who this is for
- Developers who've used ChatGPT/Claude and want to *automate* with code.
- Anyone confused by the agentic-AI buzzword soup (agents, RAG, MCP, tools, orchestration).
- People who want to run AI **privately and for free** on their own machine.

## The 30-second mental model
An **agent** = a language model + the ability to **use tools** + a **loop** that decides what to do next.
That's it. The rest is ergonomics.

```
you ──▶ agent loop ──▶ calls tools (search, code, calc) ──▶ model reasons ──▶ answer
                    ▲_____________________________________│
```

## Pick your path

**Path A — "I've never run a model."**
1. [01 Run AI Locally with Ollama](01-local-models-ollama/README.md) — free, private inference.
2. [02 Build Your First Agent](02-your-first-agent/README.md) — understand the loop.

**Path B — "I want production-grade agents."**
1. [03 LangGraph](03-langchain-langgraph/README.md) — stateful agent graphs.
2. [05 MCP](05-mcp-servers/README.md) — give agents real tools the standard way.
3. [08 Deploy](08-deploy-agents/README.md) — eval, guardrails, cost.

**Path C — "I want agents that collaborate."**
1. [04 AutoGen multi-agent](04-multi-agent-autogen/README.md).

**Always useful:**
- [07 Prompt Engineering](07-prompt-engineering/README.md) — the skill under everything.
- [06 RAG](06-rag-llamaindex/README.md) — ground agents in your own data.
- [09 Agent Skills](09-ai-skills/README.md) — package capabilities for reuse.

## What you need
- Python 3.10+ (free).
- For 01: [Ollama](https://ollama.com) (free, ~200MB).
- For cloud tutorials: an API key from OpenAI/Anthropic (optional — 01/02 work fully local).

No paid accounts required to finish Paths A. That's deliberate.

## A note on hype
Most "agent" demos are toys. The tutorials here bias toward things you can **ship**: clear tool interfaces, error handling, cost awareness, and evaluation. Read [08](08-deploy-agents/README.md) before you trust an agent with anything important.

→ Next: [01 Run AI Locally with Ollama](01-local-models-ollama/README.md)
