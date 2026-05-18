import pytest
import torch

from app.config import ModelConfig
from app.model import MiniGPT


def test_model_outputs_logits_for_each_position():
    config = ModelConfig(block_size=8, embedding_dim=16, num_heads=4, num_layers=1)
    model = MiniGPT(vocab_size=10, config=config)

    logits = model(torch.tensor([[1, 2, 3, 4]]))

    assert logits.shape == (1, 4, 10)


def test_context_overflow_handled():
    config = ModelConfig(block_size=2, embedding_dim=16, num_heads=4, num_layers=1)
    model = MiniGPT(vocab_size=10, config=config)

    with pytest.raises(ValueError, match="block_size"):
        model(torch.tensor([[1, 2, 3]]))
