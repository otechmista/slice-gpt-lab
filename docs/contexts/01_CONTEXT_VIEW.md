# CONTEXT VIEW - SLICE_GPT_LAB
(Problem, Business Intent, Boundaries)

## Instructions for AI

- Do NOT generate code.
- Do NOT define architecture.
- Do NOT invent business rules.
- Ask questions when required information is missing.
- Keep statements short, explicit, and testable.
- Mark unknowns as `TBD` instead of guessing.

---

## System Name

Slice GPT Lab

---

## Problem

Describe the problem in plain language.

- Current situation: The user already programs but does not fully understand how conversational AI models internally work.
- Pain: Most tutorials abstract the real mechanics behind GPT-like models. The user wants practical understanding of the training and inference process.
- Desired change: The system should allow the user to study and observe the complete lifecycle of a minimal conversational transformer model.

---

## Users

List all actors.

| Actor Type | Actor | Needs / Uses |
|---|---|---|
| Human user | Developer / Student | Understand how GPT-like models are trained and executed |
| System | Training runtime | Execute training and inference loops |
| System | Tokenizer | Convert text into token IDs |
| System | Transformer model | Predict the next token |
| System | Optimizer | Update weights during training |
| System | Storage layer | Persist trained model weights |
| External integration | PyTorch | Tensor operations and automatic differentiation |

---

## Goals

What must be achieved:

- Create a minimal GPT-like conversational model for study purposes
- Understand the internal stages of training and inference
- Generate a physical model artifact (`.pt`) after training
- Observe token prediction behavior during inference
- Understand how embeddings, attention, loss, and backpropagation interact

---

## Non-Goals

What is explicitly not part of the system:

- Production-grade conversational quality
- Large-scale distributed training
- GPU optimization
- RLHF or alignment training
- Multi-modal support
- Enterprise deployment

---

## Business Rules - High Level

Rules that affect behavior:

- The model must use causal next-token prediction
- Training must use explicit loss calculation and weight updates
- The system must expose all main learning stages in a readable form
- The model artifact must be serializable and reloadable
- The system must prioritize clarity over performance
- Unknown or unsupported behaviors must be explicit instead of hidden
- The assistant must answer only about the fictional pizzeria The Slice Lab
- Dataset examples and public answers must be in English only
- Inference must use the trained model checkpoint instead of hardcoded answer rules
- If the prompt is outside the pizzeria domain, the desired learned answer is: `I do not know how to answer that.`

For programming AI:

- Each rule must be implementable or reviewable.
- If a rule needs exact values, statuses, limits, or permissions, write them here.
- Do not leave policy decisions for the code generation phase.

---

## Constraints

| Type | Constraint |
|---|---|
| Technical | Must run locally on consumer hardware |
| Technical | Must use PyTorch |
| Technical | Must remain small enough for study and debugging |
| Technical | Model architecture must remain understandable by a single developer |
| Business | Pure educational purpose |
| Business | No production deadline |
| Legal / Compliance | No sensitive or private training data |
| Operational | Training should complete in minutes instead of days |
| Operational | Logs and outputs should remain human-readable |

---

## System Boundaries

Inside the system:

- Tokenization
- Embedding generation
- Positional representation
- Self-attention
- Transformer forward pass
- Loss calculation
- Backpropagation
- Weight persistence
- Text generation

Outside the system:

- Distributed GPU orchestration
- Production inference serving
- Large-scale dataset management
- Reinforcement learning pipelines
- Human feedback training
- Enterprise observability systems

---

## Data and Domain Terms

| Term / Entity | Meaning | Important Fields or States |
|---|---|---|
| Token | Numerical representation of text | token_id |
| Vocabulary | All supported tokens | vocab_size |
| Embedding | Dense vector representation of a token | embedding_dimension |
| Attention | Context relevance calculation | query, key, value |
| Transformer Block | Main processing unit | attention, feed-forward, normalization |
| Loss | Prediction error measurement | cross_entropy |
| Weight | Learned numerical parameter | tensor values |
| Checkpoint | Persisted model state | model_state_dict |
| Prompt | Input text for inference | input_tokens |
| Inference | Token generation process | logits, probabilities |

---

## Risks and Unknowns

| Item | Impact | Required Decision / Question |
|---|---|---|
| Tokenizer complexity | May obscure learning concepts | Should tokenizer remain character-based or move to BPE later? |
| Dataset size | Larger datasets reduce explainability | What is the acceptable maximum dataset size for study? |
| Attention visualization | Harder to understand internally | Should internal attention weights be exposed visually? |
| Hardware limitations | Slow training on CPU | Is GPU acceleration required later? |
| Model architecture depth | Excessive complexity harms understanding | What is the maximum acceptable transformer depth? |

---

## Readiness Gate

AI must answer before moving to `02_CONTAINER_VIEW.md`:

- Is the problem clear? yes - The objective is educational understanding of GPT-like internals
- Are users and actors identified? yes - Human, runtime, tokenizer, optimizer, and persistence actors are defined
- Are goals and non-goals separated? yes - Educational goals are isolated from production concerns
- Are high-level business rules explicit? yes - Core behavioral expectations are defined
- Are system boundaries clear? yes - Training internals are included while production systems are excluded
- Can architecture be designed without inventing requirements? yes - Core educational requirements are sufficiently defined

Decision:

- READY: yes
- Blockers: none

