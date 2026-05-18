# CONTAINER VIEW - SLICE_GPT_LAB
(System Structure, Architecture, Data Flow)

## Instructions for AI

- Do NOT generate code.
- Do NOT change business rules from `01_CONTEXT_VIEW.md`.
- Do NOT add components unless they satisfy a stated goal, rule, or constraint.
- Prefer the simplest architecture that can be tested and evolved.
- Keep responsibilities separated and named by purpose.
- Mark unknowns as `TBD` instead of guessing.

---

## Inputs

This view must be based on:

- `01_CONTEXT_VIEW.md`
- Existing architecture notes: none
- Existing repository structure: none

---

## Architecture Style

Selected style:

- modular monolith / educational script-based system

Justification:

- The system is for study, not production.
- All steps should be visible in one local project.
- The architecture must be simple enough for one developer to inspect.
- The training, inference, and persistence flow can run locally.
- Separating responsibilities into modules improves learning without adding service complexity.

Rejected alternatives:

| Alternative | Why rejected |
|---|---|
| microservices | Adds infrastructure complexity without supporting the educational goal |
| event-driven | No asynchronous business workflow is required |
| distributed training | Too complex for the stated study purpose |
| production inference service | Outside the system boundaries |
| Ollama-first runtime | Hides the model internals that the user wants to understand |

---

## System Blocks

List all major blocks.

| Block | Responsibility | Technology / Location | Owns Data? |
|---|---|---|---|
| Dataset Loader | Load the small training text dataset | Python module / `dataset.py` | no |
| Tokenizer | Convert text to token IDs and token IDs back to text | Python module / `tokenizer.py` | yes - vocabulary mapping |
| Batch Builder | Create input and target token sequences for next-token training | Python module / `batch.py` | no |
| Mini GPT Model | Execute embeddings, positional representation, transformer blocks, and logits generation | PyTorch module / `model.py` | yes - model weights |
| Training Loop | Run forward pass, calculate loss, backpropagate, and update weights | Python module / `train.py` | no |
| Checkpoint Manager | Save and load model weights and tokenizer metadata | Python module / `checkpoint.py` | yes - checkpoint files |
| Inference Loop | Generate text token by token from a prompt | Python module / `infer.py` | no |
| Study Logs | Expose loss, generated samples, and training progress | Console output / optional log file | yes - training observations |

For programming AI:

- A block should have one primary reason to change.
- Do not hide business rules inside infrastructure blocks.
- Name external systems as integrations, not internal blocks.

---

## Data Flow

Describe the main flow step by step:

1. The user starts the training command.
2. Dataset Loader reads a small local text dataset.
3. Tokenizer builds or loads the vocabulary.
4. Tokenizer converts the training text into token IDs.
5. Batch Builder creates input sequences and target sequences.
6. Mini GPT Model receives input token IDs.
7. Mini GPT Model converts tokens into embeddings.
8. Mini GPT Model adds positional information.
9. Mini GPT Model applies causal self-attention and feed-forward layers.
10. Mini GPT Model outputs logits for the next-token prediction.
11. Training Loop calculates cross-entropy loss against target tokens.
12. Training Loop runs backpropagation.
13. Optimizer updates model weights.
14. Study Logs show training loss and optional sample output.
15. Checkpoint Manager saves the trained model artifact as `.pt`.

Secondary flows:

- Model inference flow: User provides a prompt, Inference Loop formats it as a chat transcript, Tokenizer encodes it, Mini GPT Model predicts the next token repeatedly, Tokenizer decodes the result into text, and Inference Loop extracts the assistant answer.
- Unknown-domain flow: User provides a prompt outside The Slice Lab pizzeria domain, and the desired answer must be learned from dataset examples instead of hardcoded rules.
- Checkpoint reload flow: Checkpoint Manager loads `.pt` weights and tokenizer metadata, then Inference Loop uses the restored model.
- Study inspection flow: Training Loop exposes loss values and sample generations so the user can observe learning behavior.

---

## External Integrations

| System | Purpose | Protocol / SDK | Auth | Failure Impact |
|---|---|---|---|---|
| PyTorch | Tensor operations, neural network layers, autograd, optimizer | Python SDK | none | Training and inference cannot run |
| Local file system | Read dataset and save model artifact | File I/O | operating system permissions | Dataset or checkpoint cannot be loaded or saved |

---

## Persistence and State

| Data | Owner | Storage | Retention / Lifecycle | Consistency Rule |
|---|---|---|---|---|
| Training dataset | Dataset Loader | Local text file or inline text | Kept while studying | Source of truth for training examples |
| Vocabulary mapping | Tokenizer | Checkpoint metadata or local file | Must match the trained model | Source of truth for encoding and decoding |
| Model weights | Mini GPT Model / Checkpoint Manager | `.pt` file | Saved after training | Source of truth for learned behavior |
| Training loss logs | Study Logs | Console or optional log file | Temporary or manually saved | Derived from each training step |
| Generated samples | Inference Loop | Console output | Temporary | Derived from current model state |

---

## Failure Scenarios

| Failure | Impact | Handling Strategy | User/System Result |
|---|---|---|---|
| Dataset missing | Training cannot start | Reject with clear error | User sees missing dataset message |
| Dataset too small | Model may memorize or generate poor output | Allow but warn in logs | Training runs with limited learning |
| Tokenizer mismatch | Loaded model produces invalid output | Reject checkpoint or require matching metadata | Inference does not proceed |
| Checkpoint save failure | Model artifact is not created | Log error and stop after training | User knows model was not persisted |
| Checkpoint load failure | Inference cannot start | Reject with clear error | User sees invalid or missing checkpoint message |
| Loss becomes NaN | Training becomes invalid | Stop training and log failure | User sees numerical instability message |
| Prompt contains unknown token | Encoding fails or output is incomplete | Use known tokenizer rules or reject input | User sees unsupported character/token message |
| CPU training is slow | Study feedback is delayed | Keep model and dataset small | Training remains usable on local hardware |

---

## Trade-offs

| Decision | Benefit | Cost / Risk |
|---|---|---|
| Use PyTorch | Makes autograd and tensor operations visible but manageable | Some low-level math is abstracted |
| Use character-level tokenizer first | Simple to understand and debug | Less realistic than production tokenizers |
| Save `.pt` checkpoint | Easy to inspect and reload in PyTorch | Not directly usable in Ollama |
| Keep one local project | Easy to follow the full flow | Not production-like |
| Use minimal Transformer | Preserves GPT-like core behavior | Output quality will be poor |
| Prioritize readability | Improves learning | Reduces performance |

---

## Constraints Applied

Explain how context constraints shaped the architecture:

- Pure educational purpose -> architecture avoids production services and deployment complexity
- Must understand internal stages -> training and inference are separated into readable blocks
- Must generate a model artifact -> Checkpoint Manager is included
- Must run locally -> model size, dataset size, and training loop remain small
- Must use PyTorch -> PyTorch is the main external dependency
- No sensitive data -> dataset remains local, artificial, and small
- Human-readable learning process -> Study Logs are included as a first-class block

---

## Readiness Gate

AI must answer before moving to `03_COMPONENT_VIEW.md`:

- Are all system blocks named and necessary? yes - each block supports training, inference, persistence, or learning visibility
- Are responsibilities separated? yes - dataset, tokenizer, model, training, checkpointing, and inference are separated
- Is data flow clear enough to implement later? yes - both training and inference flows are described step by step
- Are integrations and failure points explicit? yes - PyTorch and local file system are listed with failure impacts
- Are storage/state ownership rules clear? yes - dataset, vocabulary, weights, logs, and samples have owners
- Can component behavior be specified without changing architecture? yes - components can now be detailed independently

Decision:

- READY: yes
- Blockers: none

