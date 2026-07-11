# AI Engineering Hub — Agentic AI & AI Programming Tutorials

A free, open, **research-backed** curriculum for people who want to actually *build* with AI agents — not just chat with them. Every tutorial has runnable code, copy-paste setup, and honest tradeoffs.

> Why this exists: the agentic-AI space is loud and full of hype. This repo is the opposite — practical, tested, and grounded in what the ecosystem actually uses (Ollama, LangChain/LangGraph, AutoGen, MCP, LlamaIndex). Stars on those projects are the demand signal; the tutorials follow it.

## What you'll learn

| # | Tutorial | Teaches | Demand signal |
|---|----------|---------|---------------|
| 00 | [Start Here](00-start-here.md) | How to use this repo + pick your path | — |
| 01 | [Run AI Locally with Ollama](01-local-models-ollama/README.md) | Private, free inference on your machine | Ollama · 176k★ |
| 02 | [Build Your First Agent (from scratch)](02-your-first-agent/README.md) | ReAct loop, tools, no frameworks | Foundations |
| 03 | [Production Agents with LangGraph](03-langchain-langgraph/README.md) | Stateful graphs, memory, human-in-loop | LangChain 141k★ · LangGraph 37k★ |
| 04 | [Multi-Agent Systems with AutoGen](04-multi-agent-autogen/README.md) | Agent teams that solve tasks together | AutoGen 60k★ |
| 05 | [MCP: Build a Tool Server](05-mcp-servers/README.md) | The new standard for agent tool-use | MCP 88k★ |
| 06 | [RAG with LlamaIndex](06-rag-llamaindex/README.md) | Give agents knowledge from your docs | LlamaIndex 51k★ |
| 07 | [Prompt Engineering That Works](07-prompt-engineering/README.md) | The skill under everything | — |
| 08 | [Ship Agents to Production](08-deploy-agents/README.md) | Eval, guardrails, cost, observability | — |
| 09 | [Agent Skills](09-ai-skills/README.md) | Reusable capability packages | Anthropic skills 160k★ |

## How to use it
Start at `00-start-here.md`. If you've never run a model, do 01 → 02. If you want production patterns, jump to 03/04/05. Every folder is self-contained.

## Philosophy
- **Run it, don't just read it.** Every code block is tested.
- **Show the tradeoffs.** Frameworks are not always the answer (02 builds one with zero deps).
- **Local-first.** Privacy and cost matter; 01 gets you free local inference.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections and new tutorials welcome — especially ones with runnable code.

## License
MIT. Use it, fork it, teach with it.
