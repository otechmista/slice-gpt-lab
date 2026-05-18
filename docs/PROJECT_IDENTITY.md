# Slice GPT Lab

Slice GPT Lab is a personal and didactic study project for understanding how a tiny GPT-like language model works from end to end.

It uses a fictional pizzeria domain, The Slice Lab, so the project stays small, memorable, and easy to inspect. The goal is not to create a powerful assistant. The goal is to make the main ideas behind generative AI visible in code.

## Name

Project name:

```txt
Slice GPT Lab
```

Repository or folder name suggestion:

```txt
slice-gpt-lab
```

Current technical model identifier:

```txt
slice-gpt-lab
```

The model identifier is used by the API examples and tests. Rename it only when intentionally changing the public contract.

## Learning Promise

After studying this project, a person should be able to explain:

- how text becomes token IDs
- how batches are built for next-token prediction
- how embeddings and positions create model input
- how causal attention blocks future tokens
- how logits become probabilities
- how loss measures prediction error
- how backpropagation updates weights
- how a checkpoint saves learned parameters
- how inference generates text one token at a time
- how a small local model can be exposed through an OpenAI-style HTTP API

## Study Order

Use this path:

1. Read [00_course_guide.md](00_course_guide.md).
2. Read [14_file_by_file_lessons.md](14_file_by_file_lessons.md).
3. Follow the concept lessons from [01_introduction.md](01_introduction.md) to [15_simple_context_model.md](15_simple_context_model.md).
4. Use [diagrams/README.md](diagrams/README.md) to visualize the flows.
5. Read the architecture views in [contexts/](contexts/) before changing behavior.
6. Open the matching files in `app/`.
7. Run the tests and scripts.

## Existing Documents

Architecture and decision views:

- [contexts/01_CONTEXT_VIEW.md](contexts/01_CONTEXT_VIEW.md): problem, goals, boundaries, and business rules.
- [contexts/02_CONTAINER_VIEW.md](contexts/02_CONTAINER_VIEW.md): runtime containers and responsibilities.
- [contexts/03_COMPONENT_VIEW.md](contexts/03_COMPONENT_VIEW.md): internal components and ownership.
- [contexts/04_CODE_VIEW.md](contexts/04_CODE_VIEW.md): source layout, contracts, commands, implementation rules, and tests.

Concept lessons:

- [01_introduction.md](01_introduction.md): project goal and main ideas.
- [02_how_llms_work.md](02_how_llms_work.md): high-level GPT-like flow.
- [03_tokenization.md](03_tokenization.md): text to token IDs.
- [04_embeddings.md](04_embeddings.md): token IDs to vectors.
- [05_self_attention.md](05_self_attention.md): causal self-attention.
- [06_transformer_blocks.md](06_transformer_blocks.md): transformer block structure.
- [07_forward_pass.md](07_forward_pass.md): model input to logits.
- [08_loss_and_backpropagation.md](08_loss_and_backpropagation.md): loss and learning.
- [09_training_loop.md](09_training_loop.md): training orchestration.
- [10_inference.md](10_inference.md): autoregressive generation.
- [11_checkpoint_and_weights.md](11_checkpoint_and_weights.md): saving and loading weights.
- [12_openai_api_layer.md](12_openai_api_layer.md): OpenAI-style API.
- [13_limitations_of_the_model.md](13_limitations_of_the_model.md): limits of this mini model.
- [15_simple_context_model.md](15_simple_context_model.md): messages, context, tokens, and context window.

Code walkthrough:

- [14_file_by_file_lessons.md](14_file_by_file_lessons.md): how each source file contributes to the system.

Diagrams:

- [diagrams/README.md](diagrams/README.md): index of visual study diagrams.

## Guiding Principle

Every file should help the reader answer one practical question:

```txt
What is this part doing in a GPT-like system?
```

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: this is the entry point for the study path.

Next: [Course Guide](00_course_guide.md) turns that promise into a study route.

<!-- COURSE_THREAD_END -->
