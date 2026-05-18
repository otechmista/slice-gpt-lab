# Checkpoint and Weights

A checkpoint saves the trained model state.

## File

```txt
app/checkpoint.py
```

## What Gets Saved

The checkpoint contains:

```txt
model_state
vocabulary
config
```

`model_state` stores learned PyTorch weights.

`vocabulary` stores the tokenizer mapping. This is required because the same character must have the same token id during inference.

`config` stores model shape values such as `block_size`, `embedding_dim`, `num_heads`, and `num_layers`.

## Where the Checkpoint Goes

Default path:

```txt
checkpoints/slice_gpt_lab.pt
```

This file is ignored by Git because it is a runtime artifact.

## Why Atomic Save Matters

`save_checkpoint()` writes to a temporary file first, then replaces the final checkpoint. That reduces the chance of leaving a half-written checkpoint behind.

## Failure Cases

The loader rejects:

- missing checkpoint files
- invalid checkpoint structure
- corrupted load attempts

This keeps inference predictable.
