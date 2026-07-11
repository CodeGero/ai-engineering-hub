# 08 — Ship Agents to Production (Eval, Guardrails, Cost)

A notebook agent that works on your screen is not a product. Production agents
fail in ways demos don't: bad inputs, runaway loops, hallucinated tool calls,
and surprise bills. This tutorial covers the non-negotiables.

## 1. Evaluate before you trust
Prompts are code — test them. A minimal eval:
```python
cases = [
  ("reset password", "account"),
  ("charged twice", "billing"),
  ("app won't open", "technical"),
]
correct = sum(
  1 for q, exp in cases
  if classify(q) == exp
)
print(f"accuracy: {correct}/{len(cases)}")
```
Track this number. When you change a prompt, re-run. Regression = red flag.

## 2. Guardrails
- **Input validation:** reject empty / huge / malicious prompts.
- **Output validation:** JSON schema check; never trust free text from a tool.
- **Tool allowlist:** an agent can only call tools you registered (see 02, 05).
- **Loop cap:** max N steps, then stop (Tutorial 02 already does this).

## 3. Cost control
- Cache embeddings (they don't change per query).
- Use small local models (Ollama, 01) for cheap steps; reserve big models for hard ones.
- Log token spend per request. A 10× cost spike usually means a loop bug.

## 4. Observability
Log every step: the prompt sent, the tool called, the observation, the cost.
You cannot debug what you don't record. (LangSmith, or just JSONL to a file.)

## 5. Human-in-the-loop for risky actions
Deploying code? Sending email? Put an `approve` node (LangGraph, 03) that pauses
for a person. Autonomous ≠ unsupervised for anything destructive.

## 6. Start small, watch it
Launch read-only. Expand permissions only after the eval holds and the logs are clean.

→ Next: [09 Agent Skills](09-ai-skills/README.md)
