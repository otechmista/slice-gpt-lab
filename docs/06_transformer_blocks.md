# Transformer Blocks: The Repeating Unit

Attention alone isn't enough. After tokens gather context from each other, something needs to *think* about that information — to transform it into something more useful.

That's where the **transformer block** comes in. It's the core repeating unit of every GPT-style model. Our tiny model stacks a few of them. GPT-4 stacks 96.

## Where This Lives

```txt
app/block.py
app/feedforward.py
```

## What a Block Does

Each transformer block has two parts that run in sequence:

1. **Self-attention:** tokens look at each other and gather context
2. **Feed-forward network:** each token independently transforms its information

After both parts, the output flows to the next block (or to the final output if this is the last block).

## The Feed-Forward Network

Think of it as a small neural network that runs on each token individually. It doesn't look at neighboring tokens — it just takes what attention collected and does further computation on it.

The structure is:

```txt
Linear layer (expand 4x)
GELU activation (adds non-linearity)
Linear layer (compress back)
Dropout (randomly zeros some values to prevent overfitting)
```

The expansion to 4x is a convention from the original Transformer paper. It gives the network room to compute more complex features before compressing back.

## Residual Connections: Keep the Original Signal

Here's a subtle but important trick. After each sub-layer (attention and feed-forward), we **add the original input back**:

```txt
output = original_input + attention(original_input)
output = output + feedforward(output)
```

This is called a **residual connection** (or skip connection).

Why does it matter? Without it, information from early layers might get lost or distorted as it passes through many blocks. With it, each block only needs to learn the *change* (residual), not rebuild everything from scratch. This makes deep networks much easier to train.

Analogy: you're taking notes while reading. Instead of rewriting everything from scratch each time, you just add highlights and annotations. The core text is always there.

## Layer Normalization: Keeping Values Stable

Before passing data to attention and feed-forward, we apply **layer normalization**. It rescales the values so they stay in a well-behaved range.

Without this, numbers can grow very large or shrink very small as they pass through many layers. Normalization keeps training stable.

## One Block, Full Picture

```txt
input
  ↓
layer norm
  ↓
self-attention
  ↓
  + (add original input back)
  ↓
layer norm
  ↓
feed-forward network
  ↓
  + (add again)
  ↓
output (goes to next block)
```

## What You Should Be Able to Explain

- What the two sub-layers in a block are
- Why residual connections exist
- What layer normalization does
- Why the feed-forward network processes each token independently (while attention processes them together)

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Self-Attention](05_self_attention.md) mixes previous context with a causal mask.

Next: [Forward Pass](07_forward_pass.md) shows how the full model produces logits.

<!-- COURSE_THREAD_END -->
