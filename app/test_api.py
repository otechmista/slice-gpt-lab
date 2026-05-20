from fastapi.testclient import TestClient

from app import api


def test_api_chat_completion_contract(monkeypatch):
    def fake_generate_text(prompt, max_tokens, temperature):
        assert "<|user|>\nhello" in prompt
        assert prompt.endswith("<|assistant|>\n")
        assert max_tokens == 3
        assert temperature == 0.7
        return "assistant: hello"

    monkeypatch.setattr(api, "generate_text", fake_generate_text)
    client = TestClient(api.app)

    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "llm-lessons",
            "messages": [{"role": "user", "content": "hello"}],
            "temperature": 0.7,
            "max_tokens": 3,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == "chatcmpl-local"
    assert body["object"] == "chat.completion"
    assert body["choices"][0]["message"]["role"] == "assistant"
    assert body["choices"][0]["message"]["content"] == "assistant: hello"


def test_api_rejects_missing_messages():
    client = TestClient(api.app)

    response = client.post(
        "/v1/chat/completions",
        json={"model": "llm-lessons", "messages": []},
    )

    assert response.status_code == 400
