# The API Layer: Talking to the Model Over HTTP

The model can answer questions from the command line. But what if you want to build a web app, a chatbot interface, or connect it to other tools?

That's where the **API** comes in. It wraps the model in an HTTP server that anyone can send requests to — just like the real OpenAI API.

## Where This Lives

```txt
app/api.py
app/schemas.py
```

## Start the Server

First, make sure you've trained the model:

```bash
python app/train.py
```

Then start the API:

```bash
uvicorn app.api:app --reload
```

Check it's alive:

```bash
curl http://127.0.0.1:8000/health
```

## Send a Question

```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "slice-gpt-lab",
    "messages": [
      {"role": "user", "content": "What pizza do you recommend?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

## What the Request Looks Like

```json
{
  "model": "slice-gpt-lab",
  "messages": [
    {"role": "user", "content": "What pizza do you recommend?"}
  ],
  "temperature": 0.7,
  "max_tokens": 100
}
```

`temperature` controls how random the output is. `0.05` = more predictable, `0.9` = more creative (and chaotic).

## What the Response Looks Like

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
        "content": "I recommend the Margherita pizza."
      },
      "finish_reason": "stop"
    }
  ]
}
```

This format intentionally mirrors the OpenAI API. If you know how to use ChatGPT's API, you already know this shape.

## Why This Format Matters

Real-world apps are built around the OpenAI API format. By following the same shape, our local model becomes a drop-in replacement — useful for testing, privacy-focused apps, or offline environments.

## The API Is Thin By Design

The API doesn't contain any model logic. It:

1. Receives the request
2. Validates it
3. Calls `generate_text()` from `app/infer.py`
4. Wraps the result in the response shape

All intelligence stays in the model pipeline. The API is just a translator between HTTP and inference.

## Explore the Auto-Generated Docs

FastAPI generates interactive documentation automatically. While the server is running, open:

```txt
http://127.0.0.1:8000/docs
```

You can test the API directly from your browser — no `curl` needed.

## What You Should Be Able to Explain

- Why an API layer is useful on top of a model
- What `temperature` and `max_tokens` control
- Why this API format mirrors OpenAI's
- Why the API should not contain model logic

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Inference](10_inference.md) generates assistant text from a trained checkpoint.

Next: [Limitations](13_limitations_of_the_model.md) explains what this tiny model still cannot do.

<!-- COURSE_THREAD_END -->
