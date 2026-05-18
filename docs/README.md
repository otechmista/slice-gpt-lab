# Slice GPT Lab Documentation

This folder is the classroom for the project.

Start here:

```txt
PROJECT_IDENTITY.md
00_course_guide.md
```

## Project Identity

- `PROJECT_IDENTITY.md`: project name, purpose, learning promise, and map to existing documents.

## Lessons

- `00_course_guide.md`: study path and project map.
- `01_introduction.md`: project goal and main ideas.
- `02_how_llms_work.md`: high-level GPT-like flow.
- `03_tokenization.md`: how text becomes token ids.
- `04_embeddings.md`: how token ids become vectors.
- `05_self_attention.md`: causal self-attention.
- `06_transformer_blocks.md`: transformer block structure.
- `07_forward_pass.md`: model input to logits.
- `08_loss_and_backpropagation.md`: loss and learning.
- `09_training_loop.md`: training orchestration.
- `10_inference.md`: model-only generation.
- `11_checkpoint_and_weights.md`: saving and loading weights.
- `12_openai_api_layer.md`: local OpenAI-style API.
- `13_limitations_of_the_model.md`: what this mini model cannot do.
- `14_file_by_file_lessons.md`: walkthrough of each source file.
- `15_simple_context_model.md`: messages, context, tokens, and context window.

## Diagrams

Mermaid diagrams live in:

```txt
diagrams/
```

Start with:

```txt
diagrams/README.md
```

## Architecture Views

Project context and implementation contracts live in:

```txt
contexts/
```

Read these when changing architecture, behavior, contracts, or commands.

- `contexts/01_CONTEXT_VIEW.md`: problem, goals, boundaries, and business rules.
- `contexts/02_CONTAINER_VIEW.md`: runtime containers and responsibilities.
- `contexts/03_COMPONENT_VIEW.md`: internal components and ownership.
- `contexts/04_CODE_VIEW.md`: implementation contracts, commands, and code rules.

