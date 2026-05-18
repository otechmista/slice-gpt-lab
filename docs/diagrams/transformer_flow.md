# Transformer Flow

Training:

```txt
dataset text
  -> tokenizer.encode
  -> token ids
  -> build_batch
  -> x inputs
  -> y targets
  -> MiniGPT(x)
  -> logits
  -> cross entropy(logits, y)
  -> loss.backward()
  -> optimizer.step()
  -> checkpoint
```

Raw model inference:

```txt
prompt
  -> tokenizer.encode
  -> MiniGPT(context)
  -> logits at last position
  -> sample next token
  -> append token
  -> repeat
  -> tokenizer.decode
```

Public inference:

```txt
prompt
  -> context builder
  -> tokenizer.encode
  -> MiniGPT(context)
  -> generated assistant tokens
  -> tokenizer.decode
  -> extracted assistant answer
```
