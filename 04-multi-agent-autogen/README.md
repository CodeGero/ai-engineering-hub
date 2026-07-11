# 04 — Multi-Agent Systems with AutoGen

One agent is a chatbot. **Several agents with different roles, talking to each
other, is a team** — and teams beat individuals on many tasks (coding + reviewing,
research + writing). AutoGen (Microsoft, 60k★) makes this pattern trivial.

## Install
```bash
pip install pyautogen
export OPENAI_API_KEY=sk-...
```

## Two agents: a coder and a critic
```python
import autogen
config = {"model": "gpt-4o-mini", "api_key": "sk-..."}

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=config,
    system_message="You write clean Python. Keep it minimal.")
critic = autogen.AssistantAgent(
    name="Critic",
    llm_config=config,
    system_message="You review code for bugs and security. Be blunt.")

user = autogen.UserProxyAgent(
    name="Human",
    code_execution_config=False,   # no auto-run; safe by default
    human_input_mode="NEVER")

group = autogen.GroupChat(agents=[coder, critic, user],
                          messages=[], max_round=4)
mgr = autogen.GroupChatManager(groupchat=group, llm_config=config)

user.initiate_chat(mgr,
    message="Write a function that finds the nth Fibonacci number efficiently.")
```
You'll see Coder propose code, Critic challenge it, Coder revise — automatically.

## When multi-agent helps
- **Generate then critique** (coder ↔ reviewer).
- **Research then write** (researcher gathers facts ↔ writer drafts).
- **Plan then execute** (planner ↔ worker).

## When it's overkill
A single well-prompted agent solves most tasks. Add agents when one role
can't hold the whole job context, or when you want adversarial checking.

## Safety
Keep `code_execution_config=False` until you trust the loop. Auto-running agent
code is how people lose servers.

→ Next: [05 MCP](05-mcp-servers/README.md)
