# Limitations of the Model

This project is educational. It is not a production chatbot.

## Main Limitations

- The tokenizer is character-level.
- The dataset is tiny.
- The model is tiny.
- Training runs for few steps.
- It runs on CPU-friendly settings.
- Model output can be broken or repetitive.
- It does not understand the world.
- It does not call external APIs.

## Why It Does Not Answer Like ChatGPT

ChatGPT-like quality comes from enormous datasets, large model capacity, long training, instruction tuning, preference optimization, safety systems, and production inference infrastructure.

This project implements the core mechanics only.

## Why There Are No Hardcoded Answers

`app/infer.py` uses the trained checkpoint for answers. It does not contain fixed pizzeria responses.

This makes the project more honest as a model study. If the answer is weak, the improvement should come from model-related changes:

- better dataset examples
- longer training
- larger model configuration
- better decoding settings
- clearer prompt format

Use this project to study model behavior, not to judge production chatbot quality.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [OpenAI API Layer](12_openai_api_layer.md) wraps inference in an OpenAI-style endpoint.

Next: [File-by-File Lessons](14_file_by_file_lessons.md) returns to the code and studies each file in detail.

<!-- COURSE_THREAD_END -->
