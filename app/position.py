"""Positional representation logic."""

import torch
from torch import nn


class PositionalEmbedding(nn.Module):
    """Add learned position vectors to token embeddings."""

    def __init__(self, block_size: int, embedding_dim: int) -> None:
        super().__init__()
        self.embedding = nn.Embedding(block_size, embedding_dim)

    def forward(self, token_embeddings: torch.Tensor) -> torch.Tensor:
        _, sequence_length, _ = token_embeddings.shape
        positions = torch.arange(sequence_length, device=token_embeddings.device)
        return token_embeddings + self.embedding(positions)
