# Attention Flow

```txt
token ids
  -> token embeddings
  -> hidden states
  -> query / key / value projections
  -> attention scores
  -> causal mask blocks future positions
  -> softmax attention weights
  -> weighted sum of values
  -> mixed context
```

Mask example:

```txt
position 0 can see: 0
position 1 can see: 0, 1
position 2 can see: 0, 1, 2
position 3 can see: 0, 1, 2, 3
```

This is why the model can train on next-token prediction without cheating.
