# The Forward Pass: Putting It All Together

The **forward pass** is what happens when you feed text into the model and it produces a prediction. All the pieces we've seen — embeddings, position, attention, feed-forward — run in sequence.

## Where This Lives

```txt
app/model.py
```

## Step by Step

The `MiniGPT` model runs these steps every time it processes a sequence:

### 1. Token Embedding
Each token ID is looked up in the embedding table and replaced with a learned vector.

```txt
[32, 17, 51] → [[0.12, -0.44, ...], [-0.73, 0.21, ...], [0.04, 0.67, ...]]
```

### 2. Positional Embedding
Position vectors are added to token vectors. This tells the model where each token is in the sequence.

```txt
token vector + position vector → combined vector
```

### 3. Transformer Blocks
The combined vectors pass through each block (attention → feed-forward). Each block refines the representation.

### 4. Final Layer Normalization
The output is normalized one more time for stability.

### 5. Output Projection
The final vectors are projected from `embedding_dim` down to `vocab_size`. This gives one score per possible next character — the **logits**.

## Shape Example

Let's trace the shapes through a real example:

```txt
Input token IDs:          [16, 64]     (16 examples, 64 tokens each)
After token embedding:    [16, 64, 48] (each token → 48-dim vector)
After position embedding: [16, 64, 48] (same shape, but position added)
After transformer blocks: [16, 64, 48] (same shape, information refined)
After output projection:  [16, 64, 54] (each token → 54 scores, one per character)
```

That final `[16, 64, 54]` tensor holds **one prediction per position per example**. At position 10, the model's guess about what character comes at position 11 is the scores at `[:, 10, :]`.

## What `block_size` Limits

`block_size` is the maximum sequence length the model accepts. If you feed in a sequence longer than `block_size`, the model rejects it.

During inference, when the generated sequence grows longer than `block_size`, the oldest tokens are dropped so we always pass in a valid-length window.

## What You Should Be Able to Explain

- The five steps of the forward pass in order
- What logits are and why there are `vocab_size` of them per position
- What the output shape `[batch, time, vocab_size]` means
- Why `block_size` matters

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Transformer Blocks](06_transformer_blocks.md) combines attention and feed-forward computation.

Next: [Loss and Backpropagation](08_loss_and_backpropagation.md) compares logits against target tokens and learns from the error.

<!-- COURSE_THREAD_END -->
