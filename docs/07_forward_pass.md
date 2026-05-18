# Forward Pass

The forward pass turns token ids into logits.

## File

```txt
app/model.py
```

## Step by Step

The `MiniGPT` model does this:

1. Validate input shape `[batch, time]`.
2. Convert token ids into token embeddings.
3. Add positional embeddings.
4. Run transformer blocks.
5. Apply final layer normalization.
6. Project hidden states into vocabulary logits.

## Shape Example

Suppose:

- batch size: `16`
- context length: `64`
- vocabulary size: `54`

Input:

```txt
[16, 64]
```

Output logits:

```txt
[16, 64, 54]
```

Each position receives one score for every possible next character.

## Why `block_size` Matters

`block_size` is the context window. If input is longer than `block_size`, the model rejects it.

During raw generation, inference keeps only the latest `block_size` tokens.
