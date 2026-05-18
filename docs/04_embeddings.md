# Embeddings

Embeddings convert token ids into learned vectors.

## File

```txt
app/embedding.py
```

## Why Embeddings Exist

A token id is just a label. The number `7` is not mathematically closer to `8` in any meaningful language sense.

The embedding layer gives each token a trainable vector:

```txt
token id -> [0.12, -0.44, 0.31, ...]
```

During training, backpropagation changes these vectors so they become useful for prediction.

## Shape Intuition

If:

- batch size is `16`
- context length is `64`
- embedding dimension is `48`

then token embeddings have shape:

```txt
[16, 64, 48]
```

That means:

- 16 examples in the batch
- 64 token positions per example
- 48 learned values per token

## Relation to GPT-like Models

All transformer language models start by embedding tokens. Larger models use much bigger embedding dimensions, but the idea is the same.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Tokenization](03_tokenization.md) turns text into token IDs.

Next: [Self-Attention](05_self_attention.md) lets each position read previous context.

<!-- COURSE_THREAD_END -->
