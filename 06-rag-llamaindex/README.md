# 06 — RAG: Ground Your Agent in Your Own Data

LLMs don't know *your* documents. **RAG (Retrieval-Augmented Generation)** fixes
that: embed your data, retrieve the relevant chunks, and feed them to the model
so it answers from facts, not memory. LlamaIndex (51k★) is the standard toolkit.

## The pipeline
```
docs → chunk → embed → store in a vector DB
query → embed → top-k similar chunks → inject into prompt → model answers
```

## Minimal RAG with LlamaIndex
```bash
pip install llama-index
```
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

docs = SimpleDirectoryReader("data/").load_data()   # drop PDFs/txt here
index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()

print(query_engine.query("What does our refund policy say about digital goods?"))
```
That's a working RAG over your files. The model can only cite what's in `data/`.

## Key levers
- **Chunk size** — too big = noise, too small = lost context. Start at 512 tokens.
- **Embedding model** — the default is fine; local models (Ollama `nomic-embed`) keep it private.
- **Top-k** — how many chunks to retrieve. 3–5 is typical.
- **Prompt** — "Answer ONLY from the context. Say 'not found' if absent." (See 07.)

## Common failure: the model ignores context
Almost always a prompt problem. Add the negative instruction from Tutorial 07 and
measure with an eval set (Tutorial 08).

## Privacy
For sensitive docs, run embeddings locally (Ollama) and use a local vector store
(`llama-index-vector-stores-qdrant` with a local Qdrant). No data leaves your box.

→ Next: [07 Prompt Engineering](07-prompt-engineering/README.md)
