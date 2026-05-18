# COMPONENT VIEW - SLICE_GPT_LAB
(Component Responsibilities, Contracts, Failure Handling)

## Inputs

- `01_CONTEXT_VIEW.md`
- `02_CONTAINER_VIEW.md`
- `04_CODE_VIEW.md`
- Current repository structure

## Component Responsibilities

| Component | File | Responsibility |
|---|---|---|
| Dataset Loader | `app/dataset.py` | Read the local training text and reject missing or empty datasets |
| Context Builder | `app/context.py` | Serialize chat messages into the same text context pattern used for training |
| Tokenizer | `app/tokenizer.py` | Build, encode, decode, and persist a character-level vocabulary |
| Batch Builder | `app/batch.py` | Create input and target windows shifted by one token |
| Embedding | `app/embedding.py` | Convert token ids into trainable vectors |
| Position | `app/position.py` | Add learned positional information to token embeddings |
| Attention | `app/attention.py` | Apply causal multi-head self-attention and block future tokens |
| Feed Forward | `app/feedforward.py` | Apply per-token nonlinear transformation |
| Transformer Block | `app/block.py` | Combine attention, feed-forward layers, normalization, and residual paths |
| Model | `app/model.py` | Produce next-token logits from token ids |
| Loss | `app/loss.py` | Calculate cross-entropy for next-token prediction |
| Sampling | `app/sampling.py` | Convert logits into the next generated token id |
| Checkpoint | `app/checkpoint.py` | Save and load model weights, config, and tokenizer metadata |
| Training | `app/train.py` | Orchestrate dataset, tokenizer, batches, model, optimizer, loss, and checkpoint |
| Inference | `app/infer.py` | Format prompts, load checkpoints, generate text with the model, and extract assistant answers |
| API | `app/api.py` | Expose thin OpenAI-style chat completion endpoint |

## Core Contracts

- Tokenizer encode rejects unsupported characters.
- Tokenizer decode rejects unknown token ids.
- Attention applies a causal mask so future positions are not visible.
- Model input shape is `[batch, time]`.
- Model output shape is `[batch, time, vocabulary]`.
- Checkpoints contain exactly `model_state`, `vocabulary`, and `config`.
- Inference rejects empty prompts.
- Public inference answers must be in English.
- Public inference must use the trained model, not hardcoded answer rules.
- Unknown-domain behavior must be learned from dataset examples.
- API delegates generation to inference and does not contain model logic.

## Readiness Gate

- Components are named and mapped to files: yes.
- Responsibilities match the container view: yes.
- Implementation can proceed without adding new architecture: yes.
- Blockers: none.

