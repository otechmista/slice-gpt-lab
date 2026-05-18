"""Thin FastAPI layer for OpenAI-compatible chat completions."""

from fastapi import FastAPI, HTTPException

try:
    from .context import ContextMessage, build_chat_context
    from .infer import generate_text
    from .schemas import (
        ChatCompletionChoice,
        ChatCompletionRequest,
        ChatCompletionResponse,
        ChatMessage,
    )
except ImportError:  # pragma: no cover - supports direct execution contexts
    from context import ContextMessage, build_chat_context
    from infer import generate_text
    from schemas import (
        ChatCompletionChoice,
        ChatCompletionRequest,
        ChatCompletionResponse,
        ChatMessage,
    )

app = FastAPI(title="Slice GPT Lab")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
def chat_completions(request: ChatCompletionRequest) -> ChatCompletionResponse:
    if not request.messages:
        raise HTTPException(
            status_code=400, detail="[ERROR] api: messages cannot be empty"
        )

    prompt = build_chat_context(
        [
            ContextMessage(role=message.role, content=message.content)
            for message in request.messages
        ],
        include_assistant_marker=True,
    )
    try:
        generated = generate_text(
            prompt=prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
        )
    except (FileNotFoundError, ValueError) as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    return ChatCompletionResponse(
        id="chatcmpl-local",
        object="chat.completion",
        model=request.model,
        choices=[
            ChatCompletionChoice(
                index=0,
                message=ChatMessage(role="assistant", content=generated),
                finish_reason="stop",
            )
        ],
    )
