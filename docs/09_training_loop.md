# Training Loop

The training loop is where the model learns.

## File

```txt
app/train.py
```

## What Happens

`train_model()` does this:

1. Load `app/dataset.txt`.
2. Build a character vocabulary.
3. Encode the dataset into token ids.
4. Create the `MiniGPT` model.
5. Create the AdamW optimizer.
6. Build random training batches.
7. Run the forward pass.
8. Calculate next-token loss.
9. Backpropagate.
10. Update model weights.
11. Save a checkpoint.

## Training Log Example

```txt
[INFO] train: vocabulary size=54
[INFO] train: sequence length=3791
[INFO] train: learning rate=0.003
[INFO] train: step=20 loss=2.6870
```

Loss usually decreases, but it may not be perfectly smooth.

## Why the Dataset Is Small

The goal is study, not quality. A small dataset trains quickly and makes it easier to inspect what is happening.

## Important Configuration

The defaults live in:

```txt
app/config.py
```

Important values:

- `block_size`: context window length
- `embedding_dim`: vector size per token
- `num_heads`: attention head count
- `num_layers`: transformer block count
- `max_steps`: number of training updates
- `learning_rate`: optimizer step size
