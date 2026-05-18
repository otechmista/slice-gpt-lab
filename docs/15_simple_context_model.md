# Simple Context Model Lesson

This lesson explains the simplest version of a GPT-style context model used in this project.

## Lesson Goal

After this lesson, you should be able to explain:

- what a GPT-like model receives as input
- why chat messages must be serialized
- what tokens are
- what a context window is
- why long conversations must be trimmed
- why this mini model is educational but not ChatGPT-quality

## What Is a GPT-like Model?

A GPT-like model is a neural network trained to predict the next token.

It does not receive meaning directly. It receives a sequence:

```txt
token_1, token_2, token_3, ...
```

During training, the model repeatedly answers this question:

```txt
Given the previous tokens, what token probably comes next?
```

## From Chat Messages to Context

Users think in messages:

```txt
system: You are a pizzeria assistant.
user: hi
assistant: Hello!
user: What pizza do you recommend?
```

The model receives one serialized text context. In this mini project, `system` is supported as a role, but normal inference keeps the prompt small and uses the same `user` to `assistant` pattern found in the dataset:

```txt
<|user|>
hi
<|assistant|>
Hello!
<|user|>
What pizza do you recommend?
<|assistant|>
```

Then the tokenizer turns that text into token ids.

In this project, `app/context.py` owns this serialization step.

## Simple Graph: Chat to Tokens

```txt
messages
  |
  v
context builder
  |
  v
"<|user|>\nhi\n<|assistant|>\n"
  |
  v
character tokenizer
  |
  v
[12, 44, 51, 18, ...]
  |
  v
MiniGPT
  |
  v
next token logits
```

## What Are Tokens?

Tokens are numeric units of text.

In real GPT systems, tokens are often pieces of words. In this study project, tokens are characters:

```txt
"pizza" -> ["p", "i", "z", "z", "a"]
```

Then each character becomes an integer id:

```txt
"pizza" -> [token_id_p, token_id_i, token_id_z, token_id_z, token_id_a]
```

Character tokens are easier to study, but they make learning harder because the model must learn spelling and meaning at the same time.

## What Is a Context Window?

The context window is the maximum amount of previous text the model can see.

In this project:

```txt
block_size = 64
```

That means the model sees at most 64 character tokens at once.

## Simple Graph: Context Window

```txt
long conversation
  |
  v
[old text][middle text][latest text]
                       ^^^^^^^^^^^^^
                       model sees this part
```

## Classroom Exercise

Open:

```txt
app/context.py
```

Find:

```txt
build_chat_context(...)
```

Then answer:

1. What role markers does it use?
2. Why does it add an assistant marker at the end?
3. What would happen if the dataset used one format and inference used another?
4. Why does a context window need a maximum size?

## Mini Summary

```txt
GPT-like chat = messages -> serialized context -> tokens -> model -> next tokens
```

The model does not magically know the conversation structure. The structure must be represented in the text it is trained on and in the text it receives during inference.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [How LLMs Work](02_how_llms_work.md) shows the whole training and inference pipeline.

Next: [Tokenization](03_tokenization.md) turns that context into token IDs.

<!-- COURSE_THREAD_END -->
