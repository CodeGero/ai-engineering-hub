# 01 — Run AI Locally with Ollama (Free, Private)

Before you pay for API calls or send your data to a cloud, run models **on your own machine**. Ollama makes this one command away. This is the cheapest, most private way to start building agents (and it powers Tutorial 02).

## Why local?
- **Free** after the download.
- **Private** — your prompts never leave your laptop.
- **No rate limits, no API keys, no account.**

## Install
```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh
# Windows: https://ollama.com/download (installer)
```
Verify:
```bash
ollama --version
```

## Pull and run a model
```bash
ollama pull llama3.2        # 3B params, ~2GB, great for dev
ollama pull qwen2.5:7b      # stronger, ~4.5GB
ollama pull phi3            # tiny + fast
ollama run llama3.2 "Explain agents in one sentence."
```

## Talk to it from Python (this is how agents call it)
```python
import urllib.request, json

def ollama_chat(prompt, model="llama3.2"):
    body = json.dumps({"model": model,
        "messages":[{"role":"user","content":prompt}],
        "stream": False}).encode()
    req = urllib.request.Request(
        "http://localhost:11434/api/chat", data=body,
        headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["message"]["content"]

print(ollama_chat("Write a Python function to reverse a string."))
```

That `ollama_chat()` is the exact primitive Tutorial 02 wraps in an agent loop.

## Common issues
- **`connection refused`** → Ollama isn't running. Start it: `ollama serve` (or just open the app).
- **Slow first response** → model is loading into RAM. Subsequent calls are faster.
- **Out of memory** → use a smaller model (`phi3` or `llama3.2`).

## Picking a model
| Need | Model | Size |
|------|-------|------|
| Fast dev/testing | phi3 | ~2.3GB |
| Balanced | llama3.2 | ~2GB |
| Best quality (consumer GPU) | qwen2.5:7b / llama3.1:8b | ~4.5–5GB |

→ Next: [02 Build Your First Agent](02-your-first-agent/README.md)
