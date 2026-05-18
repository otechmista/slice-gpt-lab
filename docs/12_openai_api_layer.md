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

Health check:

```txt
GET /health
```

Chat completion:

```txt
POST /v1/chat/completions
```

## Request Example

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

