# Transformer Blocks

A transformer block combines attention, feed-forward layers, normalization, and residual connections.

## Files

```txt
app/block.py
app/feedforward.py
```

## What the Block Does

The block receives hidden states:

```txt
[batch, time, embedding_dim]
```

Then it applies:

```txt
hidden = hidden + attention(layer_norm(hidden))
hidden = hidden + feedforward(layer_norm(hidden))
```

## Why Residual Connections Exist

The `hidden + ...` part is a residual connection.

It lets the original signal keep flowing while each layer learns an adjustment. This helps training because gradients can move through the network more easily.

## Why Layer Normalization Exists

Layer normalization keeps values in a more stable range before attention and feed-forward transformations.

## Why Feed-Forward Exists

Attention mixes information across positions. Feed-forward layers transform each position independently. Together, they let the model combine context and compute richer features.

## Relation to GPT-like Models

Large GPT models stack many transformer blocks. This project stacks only a few so the flow stays readable.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Self-Attention](05_self_attention.md) mixes previous context with a causal mask.

Next: [Forward Pass](07_forward_pass.md) shows how the full model produces logits.

<!-- COURSE_THREAD_END -->
