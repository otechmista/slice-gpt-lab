# Tokenization: Turning Text Into Numbers

Neural networks can't read. They do math. So before any text reaches the model, it has to become numbers.

**Tokenization** is that conversion step.

## What Is a Token?

A token is the smallest unit of text the model works with.

In this project, every token is a single character:

```txt
"pizza" → ['p', 'i', 'z', 'z', 'a']
```

Each character gets a unique integer ID:

```txt
['p', 'i', 'z', 'z', 'a'] → [32, 17, 51, 51, 8]
```

The mapping (which character gets which number) is built automatically from `app/dataset.txt`. Every unique character in the training data gets added to the vocabulary.

## Where This Lives

```txt
app/tokenizer.py
```

## Building the Vocabulary

The tokenizer reads all the text in the dataset and collects every unique character. If the dataset contains `a-z`, spaces, punctuation, and the special markers like `<|user|>`, all of those become vocabulary entries.

```txt
vocabulary: {' ': 0, '!': 1, ... 'a': 8, 'b': 9, ... 'z': 51, ...}
```

This gives us two lookup tables:
- `stoi`: string to integer, e.g. `'a' → 8`
- `itos`: integer to string, e.g. `8 → 'a'`

The `encode` function converts text → IDs. The `decode` function converts IDs → text.

## What Happens If You Use an Unknown Character?

If you type an emoji or an accented letter that wasn't in the training dataset, the tokenizer has no ID for it. It can't encode it. The inference code handles this by replacing unknown characters with spaces.

This is why the dataset matters. The model can only work with characters it has seen before.

## Real GPT Models Do This Differently

ChatGPT doesn't use character-level tokens. It uses a technique called **BPE (Byte Pair Encoding)** that creates tokens from common chunks of text:

```txt
"pizza" → ["piz", "za"]   (just 2 tokens instead of 5)
```

This is more efficient because shorter sequences = less memory and faster processing. But it's harder to understand. We use characters because every step is visible — you always know exactly what's happening.

## Try It

Open a Python shell and try:

```python
from app.tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer.from_text("hello world")
ids = tokenizer.encode("hello")
print(ids)
print(tokenizer.decode(ids))
```

You'll see the round-trip: text → numbers → text.

## What You Should Be Able to Explain

- Why we need tokenization at all
- Why adding a new character to the dataset changes the vocabulary
- Why the tokenizer rejects characters it hasn't seen
- How character tokenization differs from subword tokenization

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Simple Context Model](15_simple_context_model.md) shows messages becoming serialized context.

Next: [Embeddings](04_embeddings.md) turns token IDs into learnable vectors.

<!-- COURSE_THREAD_END -->
