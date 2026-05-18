"""Cross-entropy loss handling for next-token prediction."""

import torch
from torch.nn import functional as F


def next_token_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """Calculate cross-entropy over all batch/time positions."""

    if logits.ndim != 3:
        raise ValueError("[ERROR] loss: logits must have shape [batch, time, vocab]")
    if targets.ndim != 2:
        raise ValueError("[ERROR] loss: targets must have shape [batch, time]")

    batch_size, sequence_length, vocab_size = logits.shape
    return F.cross_entropy(
        logits.view(batch_size * sequence_length, vocab_size),
        targets.view(batch_size * sequence_length),
    )
