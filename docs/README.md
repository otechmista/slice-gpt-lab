# Slice GPT Lab Documentation

This folder is the classroom for the project.

Course site:

```txt
https://otechmista.github.io/mini-gpt-study/
```

Start here:

```txt
PROJECT_IDENTITY.md
00_course_guide.md
```

## Project Identity

- `PROJECT_IDENTITY.md`: project name, purpose, learning promise, and map to existing documents.

## Lessons

The course is threaded. Each lesson has a `Course Thread` section that links the previous idea to the next idea.

Recommended path:

| Step | Document | Why it comes here |
|---|---|---|
| 1 | [PROJECT_IDENTITY.md](PROJECT_IDENTITY.md) | Defines the project name, promise, and audience |
| 2 | [00_course_guide.md](00_course_guide.md) | Turns the promise into a study route |
| 3 | [01_introduction.md](01_introduction.md) | Introduces the project and pizzeria domain |
| 4 | [02_how_llms_work.md](02_how_llms_work.md) | Shows the full GPT-like flow |
| 5 | [15_simple_context_model.md](15_simple_context_model.md) | Shows how chat messages become model context |
| 6 | [03_tokenization.md](03_tokenization.md) | Turns context text into token ids |
| 7 | [04_embeddings.md](04_embeddings.md) | Turns token ids into vectors |
| 8 | [05_self_attention.md](05_self_attention.md) | Lets tokens read previous context |
| 9 | [06_transformer_blocks.md](06_transformer_blocks.md) | Combines attention with feed-forward layers |
| 10 | [07_forward_pass.md](07_forward_pass.md) | Shows how the model produces logits |
| 11 | [08_loss_and_backpropagation.md](08_loss_and_backpropagation.md) | Explains how the model learns from error |
| 12 | [09_training_loop.md](09_training_loop.md) | Puts the learning pieces into one loop |
| 13 | [11_checkpoint_and_weights.md](11_checkpoint_and_weights.md) | Saves weights, config, and vocabulary |
| 14 | [10_inference.md](10_inference.md) | Uses the checkpoint to generate text |
| 15 | [12_openai_api_layer.md](12_openai_api_layer.md) | Wraps inference in an HTTP contract |
| 16 | [13_limitations_of_the_model.md](13_limitations_of_the_model.md) | Explains the limits of the mini model |
| 17 | [14_file_by_file_lessons.md](14_file_by_file_lessons.md) | Connects each source file to the concepts |

## Diagrams

Mermaid diagrams live in:

```txt
diagrams/
```

Start with:

```txt
diagrams/README.md
```

## API Usage

The API guide lives in:

- [12_openai_api_layer.md](12_openai_api_layer.md)

It shows the local `POST /v1/chat/completions` contract used by the project.

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

