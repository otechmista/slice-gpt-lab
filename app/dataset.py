"""Dataset loading for the local study corpus."""

from pathlib import Path


def load_dataset(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"[ERROR] dataset: missing dataset file at {path}")

    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("[ERROR] dataset: dataset is empty")
    return text
