from pathlib import Path

import pytest

from app.config import ModelConfig, TrainingConfig
from app.infer import (
    extract_assistant_answer,
    format_chat_prompt,
    generate_model_text,
    generate_text,
    sanitize_for_tokenizer,
)
from app.train import train_model

TEST_OUTPUT_DIR = Path(__file__).resolve().parent.parent / ".test-output"


def artifact_path(name: str) -> Path:
    TEST_OUTPUT_DIR.mkdir(exist_ok=True)
    return TEST_OUTPUT_DIR / name


def test_empty_prompt_rejected():
    with pytest.raises(ValueError, match="prompt cannot be empty"):
        generate_text("", checkpoint_path=artifact_path("missing_empty.pt"))


def test_inference_uses_checkpoint():
    dataset_path = artifact_path("inference_dataset.txt")
    checkpoint_path = artifact_path("inference_model.pt")
    dataset_path.write_text("user: pizza\nassistant: pizza\n", encoding="utf-8")
    train_model(
        dataset_path=dataset_path,
        checkpoint_path=checkpoint_path,
        model_config=ModelConfig(
            block_size=8, embedding_dim=8, num_heads=2, num_layers=1
        ),
        training_config=TrainingConfig(batch_size=1, max_steps=1),
    )

    generated = generate_model_text(
        "user: pizza",
        checkpoint_path=checkpoint_path,
        max_tokens=2,
        temperature=1.0,
        seed=1,
    )

    assert generated.startswith("user: pizza")


def test_missing_checkpoint_fails():
    with pytest.raises(FileNotFoundError, match="missing checkpoint"):
        generate_model_text(
            "pizza", checkpoint_path=artifact_path("missing.pt"), max_tokens=1
        )


def test_format_chat_prompt_adds_training_conversation_shape():
    assert format_chat_prompt("What pizza?").endswith(
        "<|user|>\nWhat pizza?\n<|assistant|>\n"
    )


def test_extract_assistant_answer_returns_only_answer_text():
    generated = "<|user|>\nWhat pizza?\n<|assistant|>\nMargherita pizza.\n<|end|>"

    assert extract_assistant_answer(generated) == "Margherita pizza."


def test_sanitize_for_tokenizer_replaces_unsupported_characters():
    sanitized = sanitize_for_tokenizer("hi🙂", {"h", "i", " "})

    assert sanitized == "hi "


def test_generate_text_uses_checkpoint():
    dataset_path = artifact_path("generate_dataset.txt")
    checkpoint_path = artifact_path("generate_model.pt")
    dataset_path.write_text(
        "<|system|>\nAnswer pizza questions.\n"
        "<|user|>\npizza\n"
        "<|assistant|>\npizza\n"
        "<|end|>\n",
        encoding="utf-8",
    )
    train_model(
        dataset_path=dataset_path,
        checkpoint_path=checkpoint_path,
        model_config=ModelConfig(
            block_size=8, embedding_dim=8, num_heads=2, num_layers=1
        ),
        training_config=TrainingConfig(batch_size=1, max_steps=1),
    )

    generated = generate_model_text(
        "<|user|>\npizza\n<|assistant|>\n",
        checkpoint_path=checkpoint_path,
        max_tokens=2,
        temperature=0.05,
    )

    assert isinstance(generated, str)
