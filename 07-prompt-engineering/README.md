# 07 — Prompt Engineering That Actually Works

Prompts are the UI of an agent. Bad prompts = flaky agents. This is the skill
under every tutorial here. No framework fixes a vague instruction.

## The five that matter most

**1. Be specific about output format.**
```
Bad:  "Summarize this."
Good: "Summarize in 3 bullet points, each ≤ 15 words, for a busy CTO."
```

**2. Give the model a role + constraints.**
```
"You are a senior Python reviewer. Flag only security and correctness
issues. Do not rewrite style. Return a numbered list or 'NONE'."
```

**3. Show, don't just tell (few-shot).**
```
Classify the intent:
  "reset my password" -> account
  "where is my order"  -> shipping
  "I was charged twice" -> billing
Now: "the app won't open" ->
```

**4. Separate reasoning from the answer.**
```
Think step by step, then write "FINAL: <answer>" on its own line.
```
This is the backbone of the ReAct loop in Tutorial 02.

**5. Tell it what NOT to do.**
```
"Answer from the provided text only. If the answer isn't there, say
'I don't know' — never invent."
```
Critical for RAG (Tutorial 06) and any grounded agent.

## System vs user prompts
- **System:** the agent's identity, rules, tool list (set once).
- **User:** the task for this turn.
Keep the system prompt stable; vary the user prompt.

## Test your prompts
Prompts are code. Version them, run a small eval set (10–20 examples), and
measure. Tutorial 08 covers evaluation in depth.

## Red flags
- "Act as..." with no constraints → unpredictable.
- No output-format spec → you'll parse garbage.
- No negative instruction → the model fills gaps with fiction.

→ Next: [08 Ship Agents to Production](08-deploy-agents/README.md)
