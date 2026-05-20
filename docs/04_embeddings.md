# Embeddings: Giving Numbers Meaning

After tokenization, we have a list of IDs like `[32, 17, 51, 51, 8]`. But these numbers are just labels. The ID `32` for `'p'` isn't mathematically related to `33` for `'q'` in any meaningful way.

The model needs something richer than labels. It needs **vectors** — lists of numbers that can actually represent relationships between tokens.

That's what embeddings do.

## The Idea

An embedding turns each token ID into a vector of learned numbers:

```txt
token ID 32 ('p') → [0.12, -0.44, 0.31, 0.09, ...]
token ID 17 ('i') → [-0.73, 0.21, 0.88, -0.15, ...]
```

At the start of training, these vectors are random. Over time, backpropagation adjusts them until similar tokens have similar vectors, and the vectors become useful for prediction.

## Where This Lives

```txt
app/embedding.py
```

## The Lookup Table Analogy

Think of the embedding table as a giant spreadsheet:

| Token ID | Dim 1 | Dim 2 | Dim 3 | ... |
|---|---|---|---|---|
| 0 | 0.12 | -0.44 | 0.31 | ... |
| 1 | -0.73 | 0.21 | 0.88 | ... |
| 2 | 0.04 | 0.67 | -0.22 | ... |

When the model sees token ID `17`, it looks up row 17 and gets that token's vector. That vector is what flows through the rest of the network.

## What Shape Does This Produce?

If we process a batch of text sequences:

```txt
batch size: 16   (process 16 examples at once)
context length: 64   (each example is 64 tokens long)
embedding dimension: 48   (each token becomes a 48-number vector)
```

Then the output of the embedding layer has shape:

```txt
[16, 64, 48]
```

That means: 16 sequences, each with 64 tokens, each token described by 48 numbers.

## Why Embeddings Are Trainable

The embedding values start random. But because they're parameters, backpropagation updates them during training — just like any other weight in the network.

After enough training, `'z'` and `'z'` will have very similar vectors (they're the same character). Related characters like `'a'` through `'z'` will develop internal patterns. The model learns what makes each character useful for predicting the next one.

## What You Should Be Able to Explain

- Why token IDs alone aren't enough for a neural network
- What an embedding vector is
- Why embedding vectors are learned, not predefined
- What the output shape `[batch, time, embedding_dim]` means

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Tokenization](03_tokenization.md) turns text into token IDs.

Next: [Self-Attention](05_self_attention.md) lets each position read previous context.

<!-- COURSE_THREAD_END -->
