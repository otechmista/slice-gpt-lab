"""Token embedding behavior."""

import torch
from torch import nn


class TokenEmbedding(nn.Module):
    """Convert token ids into learned vectors.

    GPT-like models do not process raw token ids directly. They first look up a
    trainable vector for each token, turning discrete symbols into continuous
    values that gradient descent can adjust.
    """

    def __init__(self, vocab_size: int, embedding_dim: int) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        return self.embedding(token_ids)
