# File-by-File Lessons

Now that you understand the concepts, let's connect them to actual code.

Each lesson here matches one source file. The goal isn't just to know *what* a file does — it's to understand *why* it exists and *what question* it answers inside a GPT-style system.

---

## 1. The Training Data

**File:** `app/dataset.txt`

### What You're Learning
The model learns from examples. This file *is* those examples.

### Why It Exists
A language model can't learn without text to train on. This file contains fictional pizzeria conversations that the model will read thousands of times, learning to predict each next character.

### What to Look For
Open the file and read a few conversations. Notice:
- Every example uses the same format with `<|user|>`, `<|assistant|>`, and `<|end|>` markers
- The conversations are short and consistent
- Unknown-domain examples are also included ("I don't know how to help with that") so the model learns to decline gracefully

### Question to Answer
What happens to the character vocabulary if you add a French sentence with accents like `é` or `ç` to the dataset?

---

## 2. Loading the Data

**File:** `app/dataset.py`

### What You're Learning
Code should have one job. This file's job: read the text file, check it's valid, return the text.

### Why It Exists
The training loop shouldn't know about file paths, encoding, or validation. `dataset.py` owns that. If the file is missing or empty, it fails loudly before any other work begins.

### Question to Answer
Why is it better to fail before training starts than to fail halfway through?

---

## 3. Building the Conversation Context

**File:** `app/context.py`

### What You're Learning
The model doesn't understand "chat messages" — it understands a single long string of text. This file converts one into the other.

### Why It Exists
Before tokenization, messages must be serialized into the exact format the model was trained on:

```txt
<|user|>
What pizza do you recommend?
<|assistant|>
```

The final `<|assistant|>` without content is the signal: "continue from here as the assistant."

### Try It

```bash
python -m pytest app/test_context.py
```

### Question to Answer
What would break if training used `[USER]` markers but inference used `<|user|>` markers?

---

## 4. Tokenization

**File:** `app/tokenizer.py`

### What You're Learning
Text → numbers. This is the first real transformation in the pipeline.

### Why It Exists
Neural networks do math, not string operations. The tokenizer builds a vocabulary from the training data and provides two operations: `encode` (text → IDs) and `decode` (IDs → text).

### Try It

```python
from app.tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer.from_text("pizza is good")
print(tokenizer.encode("pizza"))
print(tokenizer.decode(tokenizer.encode("pizza")))
```

### Question to Answer
If you type a question with an emoji at inference time, what happens and why?

---

## 5. Building Batches

**File:** `app/batch.py`

### What You're Learning
The training task: given some characters, predict the next one. This file builds the actual training pairs.

### Why It Exists
Training needs input sequences and target sequences. The target is always the input shifted one position forward:

```txt
text:   p i z z a
input:  p i z z
target: i z z a
```

Position 0 sees `p` and must predict `i`. Position 1 sees `p, i` and must predict `z`. And so on.

### Question to Answer
If `block_size = 64`, how many predictions does the model make per training example?

---

## 6. Token Embeddings

**File:** `app/embedding.py`

### What You're Learning
Numbers → vectors. Token IDs are labels; embeddings give them meaning.

### Why It Exists
Token ID `32` isn't meaningfully "close to" ID `33` — they're just labels. Embeddings replace each ID with a learned vector of numbers that can capture relationships between characters.

These vectors start random and get adjusted during training. After training, the embeddings represent something useful about each character's role in the text.

### Question to Answer
Why does embedding dimension size affect how much the model can represent?

---

## 7. Positional Embeddings

**File:** `app/position.py`

### What You're Learning
The model needs to know where each token is in the sequence.

### Why It Exists
Without position information, the model would treat "pizza is good" and "good is pizza" identically — they have the same characters in different order.

Positional embeddings add a unique vector for each position (0, 1, 2, ..., block_size-1). These get added to the token embeddings:

```txt
final vector = token embedding + position embedding
```

### Question to Answer
What would go wrong if you doubled a sentence and the model couldn't tell character positions apart?

---

## 8. Self-Attention

**File:** `app/attention.py`

### What You're Learning
The heart of the transformer: how each token looks back at earlier tokens to gather context.

### Why It Exists
Predicting the next character requires understanding the previous ones. Attention creates a learned mechanism for each token to selectively gather information from earlier positions.

The causal mask ensures no token peeks at future positions — keeping training honest.

### Try It

```bash
python -m pytest app/test_attention.py
```

### Question to Answer
Why would the model perform worse if the causal mask were removed during training?

---

## 9. Feed-Forward Network

**File:** `app/feedforward.py`

### What You're Learning
After attention mixes information across positions, the feed-forward network processes each position independently.

### Why It Exists
Attention is about *relationships between tokens*. Feed-forward is about *transforming what each token now knows*. Together, they cover both aspects of processing.

The network expands to 4× the embedding dimension internally (to compute richer features), then compresses back down.

### Question to Answer
If attention handles communication between tokens, what does feed-forward handle?

---

## 10. Transformer Block

**File:** `app/block.py`

### What You're Learning
One complete block: attention + feed-forward + residual connections + layer normalization.

### Why It Exists
A transformer block is the repeating unit of GPT-style models. Our model stacks several of them. Each block sees the output of the previous one and refines it further.

### Question to Answer
What is the purpose of adding the original input back after each sub-layer (`hidden = hidden + attention(hidden)`)?

---

## 11. The Full Model

**File:** `app/model.py`

### What You're Learning
All pieces assembled into one forward pass.

### Why It Exists
This is the `MiniGPT` class. It orchestrates: embeddings → positional embeddings → transformer blocks → final normalization → output projection → logits.

### Try It

```bash
python -m pytest app/test_model.py
```

### Question to Answer
Why does the output have `vocab_size` scores per position, rather than just one score?

---

## 12. Computing Loss

**File:** `app/loss.py`

### What You're Learning
How the model measures its own prediction error.

### Why It Exists
Training needs a single number to optimize. Cross-entropy loss compares the model's predicted distribution over characters against the correct next character. Lower = better.

### Question to Answer
If the model assigned 99% probability to the correct next character, would the loss be high or low?

---

## 13. Sampling

**File:** `app/sampling.py`

### What You're Learning
The model produces scores. This file picks one character from those scores.

### Why It Exists
Logits must become a single chosen token. At low temperature, the model picks the highest-scoring character (greedy, predictable). At higher temperature, it samples probabilistically (more varied, potentially more creative — or more chaotic).

### Try It
Run inference with different `--temperature` values and notice how the output changes.

### Question to Answer
Why might very high temperature produce text that looks like random keyboard mashing?

---

## 14. Checkpoints

**File:** `app/checkpoint.py`

### What You're Learning
How trained model state is saved and reloaded.

### Why It Exists
Training stores weights in memory. Inference needs those same weights later. The checkpoint saves model weights, vocabulary, and config — everything needed to reconstruct and use the model.

### Try It
Run training and check that `checkpoints/slice_gpt_lab.pt` appears. Then run inference without retraining and see that it loads correctly.

### Question to Answer
Why must the vocabulary be saved alongside the model weights?

---

## 15. Training

**File:** `app/train.py`

### What You're Learning
The complete training orchestration: load data → build model → run the learning loop → save checkpoint.

### Why It Exists
Training connects everything: dataset, tokenizer, batch builder, model, loss, optimizer, logger, and checkpoint saver. It's the conductor that runs the full orchestra.

### Try It

```bash
python app/train.py
```

Watch the loss decrease (generally) over time.

### Question to Answer
Why does lower training loss not automatically mean the model will answer questions well?

---

## 16. Inference

**File:** `app/infer.py`

### What You're Learning
How a trained model generates text one character at a time.

### Why It Exists
Inference loads the checkpoint, formats your prompt, runs the autoregressive generation loop, and extracts the assistant's answer. This is where training becomes useful.

### Try It

```bash
python app/infer.py --prompt "What pizza do you recommend?"
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
```

### Question to Answer
Why is the `--raw-model` flag useful for studying model behavior?

---

## 17. API

**Files:** `app/api.py`, `app/schemas.py`

### What You're Learning
How to expose a local model through an HTTP interface anyone can use.

### Why It Exists
An API turns the model into a service. `api.py` handles routes and HTTP logic. `schemas.py` defines the exact shape of requests and responses — matching the OpenAI API format.

### Try It

```bash
uvicorn app.api:app --reload
```

Then visit `http://127.0.0.1:8000/docs` for interactive documentation.

### Question to Answer
Why should the API not contain any model logic? What would break if it did?

---

## 18. Tests

**Files:** `app/test_*.py`

### What You're Learning
How to verify that code behaves as expected — and how tests serve as living documentation.

### Why They Exist
Tests protect the project as you experiment. If you change the tokenizer, the tests tell you immediately whether the rest of the system still works.

### Try It

```bash
python -m pytest
```

All tests should pass. If one fails, read the error message — it's a clue about what changed.

### Question to Answer
How do tests help you understand expected behavior, even before reading the source code?

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Limitations](13_limitations_of_the_model.md) sets expectations about quality and scope.

Next: [Mermaid Diagrams](diagrams/README.md) adds visual maps for the same flows.

<!-- COURSE_THREAD_END -->
