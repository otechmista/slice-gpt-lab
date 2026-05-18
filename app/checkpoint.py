"""Checkpoint save/load behavior for model weights and tokenizer metadata."""

from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

import torch

try:
    from .config import ModelConfig
    from .model import MiniGPT
    from .tokenizer import CharacterTokenizer
except ImportError:  # pragma: no cover - supports script execution
    from config import ModelConfig
    from model import MiniGPT
    from tokenizer import CharacterTokenizer


def save_checkpoint(
    path: Path,
    model: MiniGPT,
    tokenizer: CharacterTokenizer,
    config: ModelConfig,
) -> None:
    """Persist weights and metadata together so inference can be restored."""

    path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = {
        "model_state": model.state_dict(),
        "vocabulary": tokenizer.to_dict(),
        "config": config.to_dict(),
    }

    with NamedTemporaryFile(delete=False, dir=path.parent, suffix=".tmp") as tmp:
        tmp_path = Path(tmp.name)
    try:
        torch.save(checkpoint, tmp_path)
        tmp_path.replace(path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def load_checkpoint(path: Path) -> tuple[MiniGPT, CharacterTokenizer, ModelConfig]:
    if not path.exists():
        raise FileNotFoundError(f"[ERROR] checkpoint: missing checkpoint at {path}")

    try:
        checkpoint: dict[str, Any] = torch.load(
            path, map_location="cpu", weights_only=False
        )
    except Exception as error:
        raise ValueError("[ERROR] checkpoint: failed to load checkpoint") from error

    required_keys = {"model_state", "vocabulary", "config"}
    if set(checkpoint) != required_keys:
        raise ValueError("[ERROR] checkpoint: invalid checkpoint structure")

    tokenizer = CharacterTokenizer.from_dict(checkpoint["vocabulary"])
    config = ModelConfig(**checkpoint["config"])
    model = MiniGPT(tokenizer.vocab_size, config)
    model.load_state_dict(checkpoint["model_state"])
    model.eval()
    return model, tokenizer, config
