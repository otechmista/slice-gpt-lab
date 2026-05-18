# Introduction

Slice GPT Lab is an educational project for learning how a tiny GPT-like model works.

The project is not trying to compete with ChatGPT. It is a study system. The purpose is to make the hidden steps visible:

- text becomes token ids
- token ids become vectors
- vectors receive position information
- attention mixes previous context
- the model predicts the next token
- loss measures the prediction error
- backpropagation updates weights
- a checkpoint saves the learned state
- inference generates text one token at a time

## The Pizzeria Domain

The training dataset is about a fictional pizzeria called The Slice Lab.

The dataset and public prompts are in English only.

Inference is model-only. `app/infer.py` does not contain hardcoded pizzeria answers. It formats the prompt as:

```txt
<|user|>
<question>
<|assistant|>
```

Then the trained checkpoint generates the answer character by character.

A tiny character-level model trained in minutes cannot reliably behave like a full GPT model. If it produces weak text, the lesson is not that inference needs hardcoded answers. The lesson is that model quality depends on data, scale, training time, and decoding.

## What You Should Notice

When you run training, the loss should generally go down. That does not mean the model became intelligent. It means the model got better at predicting characters from this tiny dataset.

That distinction matters. GPT-like mechanics and GPT-like product quality are different things.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Course Guide](00_course_guide.md) sets the route and commands.

Next: [How LLMs Work](02_how_llms_work.md) zooms out to the full GPT-like flow.

<!-- COURSE_THREAD_END -->
