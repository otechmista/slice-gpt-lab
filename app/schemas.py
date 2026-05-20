"""OpenAI-compatible API request and response contracts."""

from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = "llm-lessons"
    messages: list[ChatMessage]
    temperature: float = 0.8
    max_tokens: int = 80


class ChatCompletionChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: str


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    model: str
    choices: list[ChatCompletionChoice]
