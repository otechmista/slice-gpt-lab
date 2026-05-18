# Loss and Backpropagation

Training needs a way to measure error. This project uses cross-entropy loss.

## File

```txt
app/loss.py
```

## What Loss Compares

The model outputs logits:

```txt
[batch, time, vocab]
```

The targets contain the correct next token ids:

```txt
[batch, time]
```

Cross-entropy asks:

```txt
How much probability did the model assign to the correct next token?
```

Lower loss means the model is doing better on this prediction task.

## Backpropagation

Backpropagation calculates how each parameter affected the loss.

Then the optimizer updates the weights:

```txt
weights = weights - learning_rate * gradient
```

In this project, `torch.optim.AdamW` performs the update.

## NaN Protection

`app/train.py` stops if loss becomes NaN. NaN means numerical instability and makes training invalid.
