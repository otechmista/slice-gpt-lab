"""Training loop entrypoint."""

from pathlib import Path

import torch

try:
    from .batch import build_batch
    from .checkpoint import save_checkpoint
    from .config import (
        DEFAULT_CHECKPOINT_PATH,
        DEFAULT_DATASET_PATH,
        ModelConfig,
        TrainingConfig,
    )
    from .dataset import load_dataset
    from .logging_utils import log_info
    from .loss import next_token_loss
    from .model import MiniGPT
    from .tokenizer import CharacterTokenizer
except ImportError:  # pragma: no cover - supports `python app/train.py`
    from batch import build_batch
    from checkpoint import save_checkpoint
    from config import (
        DEFAULT_CHECKPOINT_PATH,
        DEFAULT_DATASET_PATH,
        ModelConfig,
        TrainingConfig,
    )
    from dataset import load_dataset
    from logging_utils import log_info
    from loss import next_token_loss
    from model import MiniGPT
    from tokenizer import CharacterTokenizer


def train_model(
    dataset_path: Path = DEFAULT_DATASET_PATH,
    checkpoint_path: Path = DEFAULT_CHECKPOINT_PATH,
    model_config: ModelConfig | None = None,
    training_config: TrainingConfig | None = None,
) -> Path:
    model_config = model_config or ModelConfig()
    training_config = training_config or TrainingConfig()

    torch.manual_seed(training_config.seed)
    generator = torch.Generator().manual_seed(training_config.seed)

    text = load_dataset(dataset_path)
    tokenizer = CharacterTokenizer.from_text(text)
    token_ids = tokenizer.encode(text)

    log_info("train", f"vocabulary size={tokenizer.vocab_size}")
    log_info("train", f"sequence length={len(token_ids)}")
    log_info("train", f"learning rate={training_config.learning_rate}")

    model = MiniGPT(tokenizer.vocab_size, model_config)
    optimizer = torch.optim.AdamW(model.parameters(), lr=training_config.learning_rate)

    for step in range(1, training_config.max_steps + 1):
        inputs, targets = build_batch(
            token_ids,
            model_config.block_size,
            training_config.batch_size,
            generator,
        )

        logits = model(inputs)
        loss = next_token_loss(logits, targets)
        if torch.isnan(loss):
            raise RuntimeError("[ERROR] train: loss became NaN")

        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()

        if step == 1 or step % training_config.log_every == 0:
            log_info("train", f"step={step} loss={loss.item():.4f}")

    save_checkpoint(checkpoint_path, model, tokenizer, model_config)
    log_info("checkpoint", f"saved at {checkpoint_path}")
    return checkpoint_path


def main() -> None:
    train_model()


if __name__ == "__main__":
    main()
