# How a Conversation Becomes Model Input

Before the model can do anything, it needs to read your question. But here's the catch: the model doesn't understand "questions" or "conversations." It only understands **a sequence of numbers**.

So how does a chat conversation become a number sequence? That's what this lesson is about.

## The Model Doesn't See a Chat — It Sees a Blob of Text

When you use ChatGPT, you see a nice chat interface: your message on the right, the AI's reply on the left. Behind the scenes, all of that gets squashed into a single flat string of text, with special markers to separate the parts:

```txt
<|user|>
What pizza do you recommend?
<|assistant|>
```

The model reads this whole string and continues it. The assistant marker at the end is a hint: "now it's your turn to respond."

This formatting is handled by `app/context.py`.

## Why the Format Has to Match the Training Data

Look at `app/dataset.txt`. Every training example uses the same markers:

```txt
<|user|>
What pizza do you recommend?
<|assistant|>
I recommend the Margherita pizza.
<|end|>
```

The model learned that text after `<|assistant|>` is the kind of thing assistants say. So when inference puts `<|assistant|>` at the end of your prompt, the model naturally continues with assistant-style text.

If training used one format and inference used a different format, the model would be confused. It's like teaching someone to respond to "Marco!" with "Polo!" — then shouting "Hey!" and wondering why they don't respond.

## What Is a Token?

Before the text reaches the model, the tokenizer splits it into small pieces called **tokens**. In this project, each character is one token:

```txt
"pizza" → ['p', 'i', 'z', 'z', 'a']
```

Then each character gets an integer ID from the vocabulary:

```txt
['p', 'i', 'z', 'z', 'a'] → [32, 17, 51, 51, 8]
```

Now the model can process numbers.

In real GPT models, tokens are usually small word-pieces (like "piz" and "za"), not single characters. That's more efficient, but harder to understand. We use characters to make every step visible.

## What Is a Context Window?

The model can't look at infinite history. It has a memory limit called the **context window**.

In this project, `block_size = 64` — meaning the model sees at most 64 characters at a time.

```txt
This is a long conversation that went on for a while...
                                        ^^^^^^^^^^^^^^
                                        model only sees this part
```

When a conversation gets too long, the oldest parts get cut off. The model always sees the most recent text.

## The Full Path: Chat → Tokens

```txt
chat messages
    ↓
context builder (app/context.py)
    ↓
"<|user|>\nWhat pizza do you recommend?\n<|assistant|>\n"
    ↓
tokenizer (app/tokenizer.py)
    ↓
[12, 44, 51, 3, 22, ...]
    ↓
MiniGPT (app/model.py)
    ↓
scores for the next character
```

## Try It Yourself

Open `app/context.py` and find the `build_chat_context` function. Then answer these questions:

1. What markers does it use to separate the user and assistant?
2. Why does the context always end with `<|assistant|>`?
3. What would break if inference used `[USER]` instead of `<|user|>`?
4. Why does a context window need a maximum size?

## Mini Summary

The model doesn't understand conversations. It understands sequences of numbers. Every message, every role, every line break gets flattened into one long string, then converted to token IDs, then fed into the model.

The structure isn't magic — it's a pattern the model learned from training data.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [How LLMs Work](02_how_llms_work.md) shows the whole training and inference pipeline.

Next: [Tokenization](03_tokenization.md) turns that context into token IDs.

<!-- COURSE_THREAD_END -->
