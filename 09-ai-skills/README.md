# 09 — Agent Skills

A **skill** is a packaged, reusable capability an agent can load on demand —
instructions + scripts + references, self-contained in a folder. Anthropic's
agent-skills ecosystem (160k★) popularized the format; the idea is portable to
any agent.

## Why skills?
- **Composable.** An agent loads "pdf-extraction" only when it needs PDFs.
- **Shareable.** Drop a skill folder into a repo; the agent discovers it.
- **Maintainable.** Update the skill, not every prompt that used it.

## Anatomy of a skill
```
my-skill/
  SKILL.md          # frontmatter (name, description) + instructions
  scripts/          # runnable helpers
  references/       # docs the agent reads when needed
```
`SKILL.md` (minimal):
```markdown
---
name: pdf-extract
description: Extract text and tables from PDFs. Use when a user uploads a PDF
  or asks to read one.
---
1. Run scripts/extract.py <file.pdf>.
2. Tables are returned as CSV; text as plain .txt.
3. If extraction fails, report the page range that errored.
```

## Writing a good skill
- The `description` is the trigger — make it specific about *when* to use it.
- Keep instructions step-by-step; the agent follows them literally.
- Put heavy reference material in `references/`, not the SKILL.md, so context stays small.

## Use it
Most agent runtimes scan a `skills/` directory at startup and expose each as a
loadable capability. The agent picks the skill whose description matches the task.

→ You've reached the end of the core curriculum. Build something, then come back
and improve a tutorial. That's how this repo gets better.
