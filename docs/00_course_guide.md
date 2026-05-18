# Course Guide

This project is a small classroom for understanding how a GPT-like system is built.

It has one answering mechanism: a tiny educational transformer model trained locally with PyTorch.

There are no hardcoded pizzeria answers in inference. The normal command formats the prompt as a chat transcript, loads the checkpoint, asks the model to generate characters, and extracts the assistant portion of the generated text.

This is closer to how GPT-style inference works, but at a very small scale. The output quality depends on the dataset, model size, training steps, and decoding settings.

## How to Study This Project

Follow this order:

1. Read this guide.
2. Read `docs/14_file_by_file_lessons.md`.
3. Read the concept chapters from `01_introduction.md` to `15_simple_context_model.md`.
4. Open each matching file in `app/`.
5. Run the tests.
6. Run training and inference.

## Lesson Format

Each lesson should answer five questions:

1. What are we learning?
2. Why does this file or concept exist?
3. How does it work step by step?
4. How can you run or inspect it?
5. What should you be able to explain after reading it?

## Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run training:

```bash
python app/train.py
```

Ask a pizzeria question with the trained model:

```bash
python app/infer.py --prompt "What pizza do you recommend?"
```

Ask an unknown-domain question with the trained model:

```bash
python app/infer.py --prompt "What is the capital of France?"
```

Run raw conversation generation for study:

```bash
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
```

Run the API:

```bash
uvicorn app.api:app --reload
```

Run tests and checks:

```bash
python -m pytest
python -m ruff check .
python -m black --check app
```

## File-by-File Lesson

| File | Lesson |
|---|---|
| `app/dataset.txt` | Shows the training examples and the English pizzeria domain |
| `app/dataset.py` | Shows how local text data enters the system |
| `app/context.py` | Shows how chat messages become one model context |
| `app/tokenizer.py` | Shows how text becomes token ids and back again |
| `app/batch.py` | Shows causal next-token training pairs |
| `app/embedding.py` | Shows how token ids become learned vectors |
| `app/position.py` | Shows how sequence position is added |
| `app/attention.py` | Shows causal self-attention and masking |
| `app/feedforward.py` | Shows the MLP inside a transformer block |
| `app/block.py` | Shows attention plus feed-forward with residual paths |
| `app/model.py` | Shows the full tiny GPT-style forward pass |
| `app/loss.py` | Shows cross-entropy next-token loss |
| `app/sampling.py` | Shows how logits become sampled token ids |
| `app/checkpoint.py` | Shows how weights and metadata are saved and loaded |
| `app/train.py` | Shows the training loop |
| `app/infer.py` | Shows model-only autoregressive generation and assistant-answer extraction |
| `app/api.py` | Shows the OpenAI-style HTTP endpoint |
| `app/schemas.py` | Shows API request and response shapes |
| `app/logging_utils.py` | Shows readable study logs |
| `app/test_*.py` | Shows executable examples of expected behavior |

For the full classroom-style walkthrough, read:

```txt
docs/14_file_by_file_lessons.md
```

For visual study diagrams, read:

```txt
docs/diagrams/README.md
```

## Key Idea

Training teaches the model to predict the next token:

```txt
input:  <|user|> What piz
target: |user|> What pizz
```

Each target is the input shifted one character to the left. This is the same core idea behind GPT-like language modeling, just at a much smaller character level.
