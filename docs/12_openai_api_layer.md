# OpenAI API Layer

The API layer exposes a small OpenAI-style chat completion endpoint.

## Files

```txt
app/api.py
app/schemas.py
```

## Run the API

```bash
uvicorn app.api:app --reload
```

Train first if the checkpoint does not exist yet:

```bash
python app/train.py
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Chat completion:

```txt
POST /v1/chat/completions
```

## Request Example With curl

```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "slice-gpt-lab",
    "messages": [
      {
        "role": "user",
        "content": "What pizza do you recommend?"
      }
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

## Request Body

```json
{
  "model": "slice-gpt-lab",
  "messages": [
    {
      "role": "user",
      "content": "What pizza do you recommend?"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 100
}
```

## Response Shape

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
        "content": "I recommend the Margherita pizza. It is simple, fresh, and the best first choice at The Slice Lab."
      },
      "finish_reason": "stop"
    }
  ]
}
```

## Design Rule

The API must stay thin. It should not contain model logic. It delegates answering to `app/infer.py`.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Inference](10_inference.md) generates assistant text from a trained checkpoint.

Next: [Limitations](13_limitations_of_the_model.md) explains what this tiny model still cannot do.

<!-- COURSE_THREAD_END -->
