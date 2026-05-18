# File-by-File Lessons

This chapter teaches the project as a sequence of small lessons.

The goal is not only to know what each file does. The goal is to understand why the file exists, how it participates in the GPT-like flow, and what you should inspect while studying it.

## Lesson 1: The Dataset

File:

```txt
app/dataset.txt
```

### What You Are Learning

You are learning what the model sees during training.

The dataset is a list of simple English conversations about the fictional pizzeria The Slice Lab.

### Why This File Exists

A language model cannot learn without examples. This file is the source text used to build the character vocabulary and training sequence.

### How It Works

The training code reads the whole file as one text string. Then the tokenizer turns every character into a token id.

Example:

```txt
<|user|>
What pizza do you recommend?
<|assistant|>
I recommend the Margherita pizza.
<|end|>
```

The model does not understand this as a human conversation. It sees a long sequence of characters and learns to predict the next character.

### Try It

Open the dataset and check:

- Are all examples in English?
- Are prices written consistently?
- Are unknown-domain examples present so the model can learn that pattern?

### Check Your Understanding

Explain why adding a new character to the dataset changes the vocabulary.

## Lesson 2: Loading Data

File:

```txt
app/dataset.py
```

### What You Are Learning

You are learning how local data enters the system.

### Why This File Exists

The training loop should not know file-reading details. `dataset.py` owns that responsibility.

### How It Works

`load_dataset(path)`:

1. Checks whether the file exists.
2. Reads text using UTF-8.
3. Rejects empty content.
4. Returns the dataset text.

### Try It

Temporarily point training to a missing file in a test and confirm it fails with a readable error.

### Check Your Understanding

Explain why empty datasets should fail before training starts.

## Lesson 3: Context Building

File:

```txt
app/context.py
```

### What You Are Learning

You are learning how chat messages become one model input.

### Why This File Exists

GPT-like models do not receive a list of Python objects. They receive a sequence of tokens. Before tokenization, the app serializes messages into text.

### How It Works

The context builder uses markers:

```txt
<|system|>
<|user|>
<|assistant|>
<|end|>
```

For a user message, it creates a prompt ending with:

```txt
<|assistant|>
```

That final marker tells the model to continue as the assistant.

### Try It

Run:

```bash
python -m pytest app/test_context.py
```

### Check Your Understanding

Explain why the dataset format and inference format must match.

## Lesson 4: Tokenization

File:

```txt
app/tokenizer.py
```

### What You Are Learning

You are learning how text becomes numbers.

### Why This File Exists

PyTorch models operate on tensors, not raw strings. The tokenizer converts between text and token ids.

### How It Works

`CharacterTokenizer.from_text(text)` builds two maps:

```txt
stoi: string token -> integer id
itos: integer id -> string token
```

Then:

```txt
encode("pizza") -> [token ids]
decode([token ids]) -> "pizza"
```

### Try It

In a Python shell:

```python
from app.tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer.from_text("pizza")
ids = tokenizer.encode("pizza")
print(ids)
print(tokenizer.decode(ids))
```

### Check Your Understanding

Explain why this tokenizer rejects characters it did not see in the training dataset.

## Lesson 4: Building Batches

File:

```txt
app/batch.py
```

### What You Are Learning

You are learning causal next-token training.

### Why This File Exists

Training needs input sequences and target sequences. The target is the input shifted one position forward.

### How It Works

For a sequence:

```txt
abcdef
```

With block size 4:

```txt
input:  abcd
target: bcde
```

The model sees `a` and should predict `b`, sees `b` and should predict `c`, and so on.

### Try It

Read `test_training.py` and `test_model.py` to see small deterministic examples.

### Check Your Understanding

Explain why the target sequence is shifted by one token.

## Lesson 5: Token Embeddings

File:

```txt
app/embedding.py
```

### What You Are Learning

You are learning how token ids become trainable vectors.

### Why This File Exists

Token ids are labels. They are not meaningful numeric values by themselves. Embeddings give each token a learned vector representation.

### How It Works

`nn.Embedding(vocab_size, embedding_dim)` creates a lookup table.

If the input shape is:

```txt
[batch, time]
```

the output shape becomes:

```txt
[batch, time, embedding_dim]
```

### Try It

Change `embedding_dim` in `ModelConfig` and watch how tensor shapes change.

### Check Your Understanding

Explain why embeddings are trainable parameters.

## Lesson 6: Position Embeddings

File:

```txt
app/position.py
```

### What You Are Learning

You are learning how the model knows token order.

### Why This File Exists

The same character can appear at many positions. The model needs a way to distinguish position 0 from position 10.

### How It Works

The file creates a learned vector for each possible position up to `block_size`.

Then it adds position vectors to token vectors:

```txt
hidden = token_embedding + position_embedding
```

### Try It

Inspect `ModelConfig.block_size` in `app/config.py`.

### Check Your Understanding

Explain what would be lost if the model had token embeddings but no position embeddings.

## Lesson 7: Causal Self-Attention

File:

```txt
app/attention.py
```

### What You Are Learning

You are learning how tokens look back at previous tokens.

### Why This File Exists

Attention lets every position mix information from earlier positions in the context window.

### How It Works

The attention module:

1. Creates query, key, and value projections.
2. Computes attention scores.
3. Applies a causal mask.
4. Converts scores into weights with softmax.
5. Mixes value vectors using those weights.

The causal mask prevents future-token cheating.

### Try It

Run:

```bash
python -m pytest app/test_attention.py
```

### Check Your Understanding

Explain why position 2 can see positions 0, 1, and 2, but not position 3.

## Lesson 8: Feed-Forward Network

File:

```txt
app/feedforward.py
```

### What You Are Learning

You are learning the second half of a transformer block.

### Why This File Exists

Attention mixes information across positions. The feed-forward network transforms each position independently.

### How It Works

The module uses:

```txt
Linear -> GELU -> Linear -> Dropout
```

The hidden size expands to `4 * embedding_dim` and then returns to `embedding_dim`.

### Try It

Find `4 * embedding_dim` in the code and connect it to the shape discussion.

### Check Your Understanding

Explain why attention and feed-forward layers solve different problems.

## Lesson 9: Transformer Block

File:

```txt
app/block.py
```

### What You Are Learning

You are learning how attention and feed-forward layers are composed.

### Why This File Exists

A transformer block is the repeated unit of GPT-like models.

### How It Works

The block applies:

```txt
hidden = hidden + attention(layer_norm(hidden))
hidden = hidden + feedforward(layer_norm(hidden))
```

The `hidden + ...` parts are residual connections.

### Try It

Change `num_layers` in `ModelConfig` and observe that the model stacks more blocks.

### Check Your Understanding

Explain what residual connections help preserve.

## Lesson 10: The Model

File:

```txt
app/model.py
```

### What You Are Learning

You are learning the full forward pass.

### Why This File Exists

This file composes embeddings, positions, transformer blocks, normalization, and logits.

### How It Works

Input:

```txt
[batch, time]
```

Output:

```txt
[batch, time, vocab_size]
```

Each position receives one score for each possible next token.

### Try It

Run:

```bash
python -m pytest app/test_model.py
```

### Check Your Understanding

Explain why logits have a vocabulary dimension.

## Lesson 11: Loss

File:

```txt
app/loss.py
```

### What You Are Learning

You are learning how the model receives a training signal.

### Why This File Exists

The model needs a scalar error value so backpropagation can update weights.

### How It Works

`next_token_loss(logits, targets)` flattens batch and time dimensions and applies cross-entropy.

### Try It

Read the shape validation in `loss.py`.

### Check Your Understanding

Explain why cross-entropy is appropriate for choosing one token from a vocabulary.

## Lesson 12: Sampling

File:

```txt
app/sampling.py
```

### What You Are Learning

You are learning how raw logits become a generated token.

### Why This File Exists

During raw model generation, the model returns scores. Sampling turns those scores into one token id.

### How It Works

The function:

1. Divides logits by temperature.
2. Applies softmax.
3. Samples one token with `torch.multinomial`.

### Try It

Compare outputs with different temperature values in `--raw-model` mode.

### Check Your Understanding

Explain what can happen when temperature is higher.

## Lesson 13: Checkpoints

File:

```txt
app/checkpoint.py
```

### What You Are Learning

You are learning how trained state is saved and restored.

### Why This File Exists

Training creates weights in memory. Inference later needs those same weights and tokenizer metadata.

### How It Works

The checkpoint stores:

```txt
model_state
vocabulary
config
```

### Try It

Run training and check that `checkpoints/slice_gpt_lab.pt` appears.

### Check Your Understanding

Explain why tokenizer metadata must be saved with the model weights.

## Lesson 14: Training

File:

```txt
app/train.py
```

### What You Are Learning

You are learning the complete learning loop.

### Why This File Exists

Training is orchestration. It connects dataset, tokenizer, batches, model, loss, optimizer, logs, and checkpointing.

### How It Works

The loop repeats:

```txt
batch -> model -> loss -> backward -> optimizer step
```

### Try It

Run:

```bash
python app/train.py
```

Watch the loss values in the console.

### Check Your Understanding

Explain why lower loss does not automatically mean ChatGPT-level quality.

## Lesson 15: Inference

File:

```txt
app/infer.py
```

### What You Are Learning

You are learning model-only autoregressive generation.

### Why This File Exists

The app should answer by loading the trained checkpoint and generating text. It should not contain fixed pizzeria answers.

### How It Works

Normal mode:

```txt
prompt -> chat formatting -> model generation -> assistant answer extraction
```

Raw mode:

```txt
prompt -> chat formatting -> tokenizer -> model -> sampling -> full generated text
```

### Try It

Normal:

```bash
python app/infer.py --prompt "What pizza do you recommend?"
```

Unknown:

```bash
python app/infer.py --prompt "What is the capital of France?"
```

Raw:

```bash
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
```

### Check Your Understanding

Explain why model-only output can be weak when the dataset, training time, or model size is too small.

## Lesson 16: API

Files:

```txt
app/api.py
app/schemas.py
```

### What You Are Learning

You are learning how the local model is exposed through an HTTP contract.

### Why These Files Exist

`api.py` exposes FastAPI routes. `schemas.py` defines request and response shapes.

### How It Works

`POST /v1/chat/completions` receives messages, builds a prompt, calls `generate_text()`, and returns an OpenAI-style response.

### Try It

Run:

```bash
uvicorn app.api:app --reload
```

Then open:

```txt
http://127.0.0.1:8000/docs
```

### Check Your Understanding

Explain why the API layer should not contain model logic.

## Lesson 17: Tests

Files:

```txt
app/test_*.py
```

### What You Are Learning

You are learning how behavior is protected.

### Why These Files Exist

Tests make the study project safer to change.

### How They Work

The tests cover:

- tokenizer round trips
- invalid tokens
- causal masks
- model output shape
- context overflow
- checkpoint usage
- API response shape
- model-only inference through checkpoint loading

### Try It

Run:

```bash
python -m pytest
```

### Check Your Understanding

Explain why tests are part of the learning material, not just a quality gate.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Limitations](13_limitations_of_the_model.md) sets expectations about quality and scope.

Next: [Mermaid Diagrams](diagrams/README.md) adds visual maps for the same flows.

<!-- COURSE_THREAD_END -->
