from app.config import ModelConfig, TrainingConfig
from app.train import train_model

from pathlib import Path

TEST_OUTPUT_DIR = Path(__file__).resolve().parent.parent / ".test-output"


def artifact_path(name: str) -> Path:
    TEST_OUTPUT_DIR.mkdir(exist_ok=True)
    return TEST_OUTPUT_DIR / name


def test_training_creates_checkpoint():
    dataset_path = artifact_path("training_dataset.txt")
    checkpoint_path = artifact_path("training_model.pt")
    dataset_path.write_text("pizza pizza pizza\n", encoding="utf-8")

    result = train_model(
        dataset_path=dataset_path,
        checkpoint_path=checkpoint_path,
        model_config=ModelConfig(
            block_size=4, embedding_dim=8, num_heads=2, num_layers=1
        ),
        training_config=TrainingConfig(batch_size=2, max_steps=2, log_every=1),
    )

    assert result == checkpoint_path
    assert checkpoint_path.exists()


def test_small_dataset_trains():
    dataset_path = artifact_path("small_dataset.txt")
    checkpoint_path = artifact_path("small_model.pt")
    dataset_path.write_text("abcdabcdabcd", encoding="utf-8")

    train_model(
        dataset_path=dataset_path,
        checkpoint_path=checkpoint_path,
        model_config=ModelConfig(
            block_size=3, embedding_dim=8, num_heads=2, num_layers=1
        ),
        training_config=TrainingConfig(batch_size=1, max_steps=1),
    )

    assert checkpoint_path.exists()
