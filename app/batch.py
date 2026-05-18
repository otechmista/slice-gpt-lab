"""Training batch generation for causal next-token prediction."""

import torch


def build_batch(
    token_ids: list[int],
    block_size: int,
    batch_size: int,
    generator: torch.Generator | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Create input and target windows shifted by one token.

    For GPT-like training, each position learns to predict the next token. If
    `x` contains tokens 0..N, `y` contains tokens 1..N+1 for the same windows.
    """

    if block_size <= 0:
        raise ValueError("[ERROR] batch: block_size must be positive")
    if batch_size <= 0:
        raise ValueError("[ERROR] batch: batch_size must be positive")
    if len(token_ids) <= block_size:
        raise ValueError("[ERROR] batch: dataset must be larger than block_size")

    max_start = len(token_ids) - block_size - 1
    starts = torch.randint(0, max_start + 1, (batch_size,), generator=generator)

    x = torch.stack(
        [torch.tensor(token_ids[start : start + block_size]) for start in starts]
    )
    y = torch.stack(
        [
            torch.tensor(token_ids[start + 1 : start + block_size + 1])
            for start in starts
        ]
    )
    return x.long(), y.long()
