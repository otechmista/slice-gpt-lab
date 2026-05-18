# Slice GPT Lab

Didactic lab for studying, in a small local codebase, the lifecycle of a GPT-like model: tokenization, causal next-token training, checkpoint persistence, and autoregressive inference.

The public domain of the app is a fictional pizzeria called The Slice Lab. The dataset and public answers are in English.

This repository is meant to be studied as a guided classroom, not used as a production AI system. The project name is **Slice GPT Lab**; the OpenAI-style model identifier is `slice-gpt-lab`.

## Study Path

Start with the project identity and learning map:

- [docs/PROJECT_IDENTITY.md](docs/PROJECT_IDENTITY.md): name, purpose, audience, and learning promise.
- [docs/00_course_guide.md](docs/00_course_guide.md): recommended study order.
- [docs/14_file_by_file_lessons.md](docs/14_file_by_file_lessons.md): file-by-file walkthrough of the code.
- [docs/diagrams/README.md](docs/diagrams/README.md): visual diagrams for training, inference, attention, checkpoints, and context.
- [docs/contexts/01_CONTEXT_VIEW.md](docs/contexts/01_CONTEXT_VIEW.md): why the project exists and what is inside or outside the system.
- [docs/contexts/02_CONTAINER_VIEW.md](docs/contexts/02_CONTAINER_VIEW.md): main runtime containers and responsibilities.
- [docs/contexts/03_COMPONENT_VIEW.md](docs/contexts/03_COMPONENT_VIEW.md): internal components and ownership.
- [docs/contexts/04_CODE_VIEW.md](docs/contexts/04_CODE_VIEW.md): implementation contracts, commands, and code rules.

## Structure

- `app/`: application code and tests.
- `docs/`: classroom-style educational documentation.
- `docs/contexts/`: architecture and contract views.

## Commands

```bash
pip install -r requirements.txt
python app/train.py
python app/infer.py --prompt "What pizza do you recommend?"
python app/infer.py --prompt "What is the capital of France?"
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
uvicorn app.api:app --reload
python -m pytest
python -m ruff check .
python -m black --check app
```

## Documentation

Start with [docs/PROJECT_IDENTITY.md](docs/PROJECT_IDENTITY.md), then follow [docs/00_course_guide.md](docs/00_course_guide.md). The `docs/` folder is organized as a file-by-file lesson.
