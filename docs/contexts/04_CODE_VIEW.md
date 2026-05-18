# CODE VIEW - SLICE_GPT_LAB
(Implementation, Structure, Contracts)

## Instructions for AI

- Generate code ONLY after `01_CONTEXT_VIEW.md`, `02_CONTAINER_VIEW.md`, and `03_COMPONENT_VIEW.md` are ready.
- Do NOT invent business rules.
- Do NOT change architecture.
- Follow existing repository patterns first.
- Keep code simple and testable.
- Include tests for documented rules, edge cases, and failures.
- List assumptions and deviations explicitly.
- This project is educational-first.
- Readability is more important than optimization.
- Explainability is more important than abstraction.
- Follow Lean Architecture principles.
- Prefer one file per domain responsibility.
- Keep the project flat and highly navigable.
- Avoid unnecessary folders.
- All application source code must stay inside `app/`.
- Create folders only when required by the runtime/tooling ecosystem.
- Avoid premature abstractions.
- Avoid enterprise patterns for this study project.

---

## Inputs

This view must be based on:

- `01_CONTEXT_VIEW.md`
- `02_CONTAINER_VIEW.md`
- `03_COMPONENT_VIEW.md`
- `AGENTS.md`
- Existing source code: none

---

## Language and Runtime

| Item | Value |
|---|---|
| Language | Python |
| Runtime / Framework | PyTorch + FastAPI |
| Package manager | pip |
| Database / Storage | Local filesystem |
| Test framework | pytest |
| Lint / Format | ruff + black |

---

## Commands

| Purpose | Command |
|---|---|
| Setup | `pip install -r requirements.txt` |
| Run training | `python app/train.py` |
| Run inference | `python app/infer.py` |
| Run API | `uvicorn app.api:app --reload` |
| Test | `python -m pytest` |
| Lint / Check | `python -m ruff check . && python -m black --check app` |
| Format | `python -m black app` |
| Build | `none` |

---

## Project Structure

```txt
slice-gpt-lab/
+-- app/
|   +-- dataset.txt                 # Small conversational dataset
|   +-- context.py                  # Chat context serialization
|   +-- config.py                   # Hyperparameters and runtime settings
|   +-- tokenizer.py                # Tokenization and vocabulary mapping
|   +-- batch.py                    # Training batch generation
|   +-- embedding.py                # Token embedding behavior
|   +-- position.py                 # Positional representation logic
|   +-- attention.py                # Self-attention and multi-head attention
|   +-- feedforward.py              # Feed-forward network behavior
|   +-- block.py                    # Transformer block orchestration
|   +-- model.py                    # Main Mini GPT model
|   +-- loss.py                     # Cross-entropy loss handling
|   +-- sampling.py                 # Token sampling strategies
|   +-- checkpoint.py               # Save/load model state
|   +-- train.py                    # Training loop orchestration
|   +-- infer.py                    # Autoregressive inference loop
|   +-- api.py                      # OpenAI-compatible API layer
|   +-- schemas.py                  # API request/response contracts
|   +-- logging_utils.py            # Logs and metrics
|   +-- test_tokenizer.py
|   +-- test_attention.py
|   +-- test_model.py
|   +-- test_training.py
|   +-- test_inference.py
|   +-- test_api.py
|
+-- docs/
|   +-- 00_course_guide.md
|   +-- 01_introduction.md
|   +-- 02_how_llms_work.md
|   +-- 03_tokenization.md
|   +-- 04_embeddings.md
|   +-- 05_self_attention.md
|   +-- 06_transformer_blocks.md
|   +-- 07_forward_pass.md
|   +-- 08_loss_and_backpropagation.md
|   +-- 09_training_loop.md
|   +-- 10_inference.md
|   +-- 11_checkpoint_and_weights.md
|   +-- 12_openai_api_layer.md
|   +-- 13_limitations_of_the_model.md
|   +-- diagrams/
|       +-- attention_flow.md
|       +-- transformer_flow.md
|
+-- requirements.txt
+-- README.md
+-- AGENTS.md
````

Rules:

* All source code must stay inside `app/`
* Keep one responsibility per file
* Keep the project intentionally flat
* Avoid folders like:

  * `services`
  * `core`
  * `shared`
  * `helpers`
  * `utils`
  * `adapters`
  * `providers`
* Prefer explicit implementations over abstractions
* Generated checkpoints must not be committed
* Runtime artifacts should remain outside source control

---

## Educational Documentation Rules

The repository is a STUDY SYSTEM.

The project must teach how GPT-like systems work internally.

Every important algorithmic step must be documented.

The `docs/` directory is mandatory.

Each documentation file must explain:

* What the component does
* Why the component exists
* What problem it solves
* How the algorithm works conceptually
* How tensor shapes change
* How it relates to GPT/Gemma/Llama-like systems
* Simplified mathematical intuition
* Simplified computational intuition

Documentation must:

* Be beginner-friendly
* Prefer intuition over academic formalism
* Explain concepts pragmatically
* Include small examples
* Include diagrams when useful

ASCII diagrams are acceptable.

---

## Code Documentation Rules

Important code sections must contain educational comments.

Document especially:

* tokenization
* embeddings
* positional representation
* attention
* causal masking
* transformer blocks
* logits
* softmax
* cross entropy
* backpropagation
* checkpoint persistence
* autoregressive generation

Comments must explain:

```txt
WHAT is happening
WHY it exists
WHAT problem it solves
HOW it relates to GPT-like models
```

Avoid comments that only restate the code.

---

## Entities and Data Types

| Entity / Type     | Description                           | Owner         |
| ----------------- | ------------------------------------- | ------------- |
| TokenId           | Integer representing a token          | tokenizer.py  |
| Vocabulary        | Token-to-id and id-to-token mapping   | tokenizer.py  |
| EmbeddingVector   | Dense numerical representation        | embedding.py  |
| HiddenState       | Transformer internal tensor state     | model.py      |
| AttentionWeights  | Context relevance matrix              | attention.py  |
| Logits            | Raw next-token prediction scores      | model.py      |
| LossValue         | Scalar training error                 | loss.py       |
| Checkpoint        | Serialized model weights and metadata | checkpoint.py |
| Prompt            | Input text for generation             | infer.py      |
| GeneratedSequence | Output token sequence                 | infer.py      |
| Context           | Serialized chat messages              | context.py    |

Core type definitions:

```txt
TokenId = int

Vocabulary:
  stoi: map[string]int
  itos: map[int]string

Checkpoint:
  model_state
  vocabulary
  config
```

---

## Public Contracts

| Contract                    | Input                | Output                | Errors                         |
| --------------------------- | -------------------- | --------------------- | ------------------------------ |
| `python app/train.py`       | dataset + config     | `.pt` checkpoint      | dataset/config/training errors |
| `python app/infer.py`       | prompt + checkpoint  | generated text        | tokenizer/checkpoint errors    |
| `POST /v1/chat/completions` | OpenAI-style request | OpenAI-style response | validation/checkpoint errors   |
| tokenizer encode            | raw text             | token ids             | unsupported token              |
| tokenizer decode            | token ids            | raw text              | invalid token id               |
| checkpoint save             | model state          | `.pt` file            | filesystem failure             |
| checkpoint load             | `.pt` file           | restored model        | corrupted checkpoint           |

Domain and language contract:

```txt
Public answers must be in English.
Inference must use the trained model checkpoint instead of hardcoded answer rules.
Input outside The Slice Lab pizzeria domain should learn -> I do not know how to answer that.
Normal inference returns the extracted assistant answer.
Raw model mode returns the full generated transcript.
```

API request example:

```json
{
  "model": "slice-gpt-lab",
  "messages": [
    {
      "role": "user",
      "content": "hello"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 100
}
```

API response example:

```json
{
  "id": "chatcmpl-local",
  "object": "chat.completion",
  "model": "slice-gpt-lab",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "generated text"
      },
      "finish_reason": "stop"
    }
  ]
}
```

---

## Implementation Rules

Enforce architecture:

* One file = one primary responsibility
* Keep tensor operations visible
* Prefer direct implementation over abstraction
* Avoid inheritance-heavy designs
* Avoid plugin systems
* Avoid dependency injection frameworks
* Avoid service locators
* Avoid hidden framework magic
* Validation belongs at input boundaries
* Tokenizer owns vocabulary consistency
* Attention masking belongs only to attention.py
* Checkpoint persistence belongs only to checkpoint.py
* Training orchestration belongs only to train.py
* Inference orchestration belongs only to infer.py
* API exposure belongs only to api.py
* API layer must remain thin
* API layer must not contain model logic
* API layer must use inference components
* Keep logs human-readable
* Keep tensor shapes observable during debugging
* Stop execution immediately on invalid tensor states

For programming AI:

* Prefer readability over DRY
* Prefer explicit tensor flow
* Prefer understandable math over optimization
* Do not add dependencies beyond:

  * torch
  * fastapi
  * uvicorn
  * pytest
  * black
  * ruff

---

## Error Handling

| Error Category | Trigger                            | Handling         | User/System Output    |
| -------------- | ---------------------------------- | ---------------- | --------------------- |
| Validation     | invalid token/config/context       | reject execution | readable error        |
| Business       | unsupported generation config      | reject request   | explicit explanation  |
| Not Found      | dataset/checkpoint missing         | stop execution   | missing file message  |
| Conflict       | tokenizer/checkpoint mismatch      | reject load      | mismatch explanation  |
| System         | NaN loss/tensor/filesystem failure | stop and log     | debugging information |

Error format:

```txt
[ERROR] <component>: <human-readable explanation>
```

Example:

```txt
[ERROR] tokenizer: token id 9999 does not exist in vocabulary
```

---

## Logging and Observability

Must include:

* training step
* loss value
* tensor shapes during debug
* generation step
* checkpoint save/load status
* vocabulary size
* sequence length
* learning rate

Must not include:

* binary tensor dumps
* unnecessary framework internals
* unrelated stack traces unless debug mode enabled

---

## Tests

Required test groups:

Business rules:

* `test_causal_mask_blocks_future_tokens`
* `test_generation_is_autoregressive`
* `test_checkpoint_restores_same_output`

Edge cases:

* `test_empty_prompt_rejected`
* `test_context_overflow_handled`
* `test_invalid_token_rejected`
* `test_small_dataset_trains`

Failure scenarios:

* `test_missing_checkpoint_fails`
* `test_nan_loss_stops_training`
* `test_tokenizer_mismatch_rejected`

Integration or contract tests:

* `test_training_creates_checkpoint`
* `test_inference_uses_checkpoint`
* `test_tokenizer_encode_decode_roundtrip`
* `test_api_chat_completion_contract`
* `test_api_rejects_missing_messages`
* `test_api_uses_checkpoint`

Test rules:

* Tests must remain deterministic
* Random seeds should be fixed
* Prefer real tensor execution over mocking
* Add regression tests for future bugs

---

## Performance and Security Constraints

Performance:

* Must run on CPU-only environments
* Training should finish in minutes
* Dataset should remain intentionally small
* Context window should remain small and observable
* Avoid hidden optimizations

Security:

* No remote execution
* No external API calls
* No dynamic code execution
* Local filesystem only
* Reject malformed checkpoints safely

Reliability:

* Save checkpoints atomically when possible
* Stop immediately on invalid tensor states
* Avoid corrupting existing checkpoints
* Inference failures must remain predictable

---

## Implementation Plan for AI

Use this order:

1. Implement config and tokenizer
2. Implement batch generation
3. Implement embeddings
4. Implement positional representation
5. Implement self-attention
6. Implement feed-forward network
7. Implement transformer block
8. Implement model forward pass
9. Implement loss handling
10. Implement training loop
11. Implement checkpoint persistence
12. Implement inference generation
13. Implement OpenAI-compatible API
14. Add logs and observability
15. Add educational documentation
16. Add tests
17. Run lint and formatting validation
18. Report assumptions and deviations

Stop if:

* Business rules become ambiguous
* Tensor dimensions become undefined
* Context behavior becomes unclear
* Checkpoint structure changes unexpectedly
* Additional folders become necessary without justification

---

## Readiness Gate

AI must answer before coding:

* Are previous views marked ready? yes - all previous views are approved
* Are contracts and data types clear? yes - model flow and API contracts are defined
* Are implementation rules clear? yes - Lean Architecture and educational rules are explicit
* Are errors and tests defined? yes - failure handling and validation tests are specified
* Are commands available? yes - runtime and validation commands are defined
* Can code be generated without inventing behavior? yes - architecture and execution behavior are fully specified

Decision:

* READY: yes
* Blockers: none

