# How LLMs Work

A GPT-like model learns by solving a simple task many times:

```txt
Given the previous tokens, predict the next token.
```

In this project the tokens are characters. In larger models, tokens are usually chunks of text created by a tokenizer such as BPE.

## The Full Flow

```txt
text
  -> tokenizer
  -> token ids
  -> batches
  -> embeddings
  -> positional embeddings
  -> transformer blocks
  -> logits
  -> loss
  -> backpropagation
  -> updated weights
```

During inference, the flow is similar, but there is no loss or backpropagation:

```txt
prompt
  -> tokenizer
  -> model
  -> logits for next token
  -> sample one token
  -> append token to prompt
  -> repeat
```

## What Logits Are

Logits are raw scores. If the vocabulary has 54 characters, the model returns 54 scores for each position. The highest or sampled score becomes the next token choice.

## Why Output Can Still Be Weak

This project uses only the trained mini model for inference. There are no hardcoded answers.

The tiny model can still produce broken text because it is very small, character-based, and trained on a tiny dataset. That is expected. GPT-like mechanics and GPT-level quality are different things.

To improve output, you can:

- add more dataset examples
- train for more steps
- increase model size carefully
- use lower temperature for less random decoding
- improve prompt formatting
