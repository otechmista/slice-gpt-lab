# Self-Attention

Self-attention lets each token decide which previous tokens matter.

## File

```txt
app/attention.py
```

## The Problem Attention Solves

To predict the next character, the model needs context.

For example:

```txt
The Slice
```

The next character depends on what came before. Attention gives each position a way to look back at earlier positions.

## Query, Key, Value

The model creates three projections:

- Query: what this token is looking for
- Key: what each token offers for comparison
- Value: the information each token can contribute

The simplified math:

```txt
scores = query @ key.T
weights = softmax(scores)
context = weights @ value
```

## Causal Mask

During training, the target answer is already present in the sequence. Without masking, the model could cheat by looking at future tokens.

The causal mask looks like this:

```txt
1 0 0 0
1 1 0 0
1 1 1 0
1 1 1 1
```

A position can see itself and the past, never the future.

## Multi-Head Attention

The model splits the embedding dimension into multiple heads. Each head can learn a different kind of relationship.

In this project:

```txt
embedding_dim = 48
num_heads = 4
head_dim = 12
```

## Relation to GPT-like Models

Causal self-attention is the central mechanism behind GPT-style text generation.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Embeddings](04_embeddings.md) turns token IDs into vectors.

Next: [Transformer Blocks](06_transformer_blocks.md) wraps attention with feed-forward layers, normalization, and residual paths.

<!-- COURSE_THREAD_END -->
