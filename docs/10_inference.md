# Inference

Inference is how the system answers prompts.

## File

```txt
app/infer.py
```

## Model-Only Answer Path

The normal command uses the trained model checkpoint:

```bash
python app/infer.py --prompt "What pizza do you recommend?"
```

Possible output after training:

```txt
I recommend the Margherita pizza.
```

Unknown-domain prompt:

```bash
python app/infer.py --prompt "What is the capital of France?"
```

The model will only answer this correctly if the dataset and training made that pattern likely. There is no hardcoded fallback in inference.

## Why Output Is Not Guaranteed

The tiny model is educational. It is not strong enough to reliably answer like ChatGPT.

If it outputs strange text, inspect:

- the dataset examples
- training loss
- checkpoint freshness
- temperature
- max token count
- model size

## Raw Conversation Path

To see the full generated conversation instead of only the extracted assistant answer:

```bash
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
```

Both normal and raw modes use the model. The difference is output formatting:

- normal mode returns only the assistant answer
- raw mode returns the full generated transcript

The generation path uses:

1. checkpoint load
2. tokenizer encode
3. model forward pass
4. logits
5. sampling
6. token append
7. tokenizer decode

The output may be strange. That is part of the lesson: architecture alone is not enough for ChatGPT-level quality.
