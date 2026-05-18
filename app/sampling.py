"""Token sampling strategies for autoregressive generation."""

import torch
from torch.nn import functional as F


def choose_next_token(logits: torch.Tensor, temperature: float = 0.8) -> int:
    """Choose one token id from logits.

    Low temperatures are decoded greedily to make the tiny study model less
    noisy. Higher temperatures use sampling so students can observe variation.
    """

    if temperature <= 0:
        raise ValueError("[ERROR] sampling: temperature must be greater than zero")
    if temperature < 0.15:
        return int(torch.argmax(logits).item())
    return sample_next_token(logits, temperature)


def sample_next_token(logits: torch.Tensor, temperature: float = 1.0) -> int:
    """Sample one token id from next-token logits."""

    if temperature <= 0:
        raise ValueError("[ERROR] sampling: temperature must be greater than zero")

    scaled_logits = logits / temperature
    probabilities = F.softmax(scaled_logits, dim=-1)
    next_token = torch.multinomial(probabilities, num_samples=1)
    return int(next_token.item())
