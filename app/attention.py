"""Causal self-attention implementation."""

import math

import torch
from torch import nn
from torch.nn import functional as F


def causal_mask(
    sequence_length: int, device: torch.device | None = None
) -> torch.Tensor:
    """Return a lower-triangular mask that blocks future tokens."""

    return torch.tril(
        torch.ones(sequence_length, sequence_length, device=device)
    ).bool()


class MultiHeadCausalSelfAttention(nn.Module):
    """Multi-head self-attention with a causal mask.

    Each token can attend only to itself and previous tokens. That constraint is
    what makes next-token prediction honest: the model cannot peek at the answer.
    """

    def __init__(self, embedding_dim: int, num_heads: int, dropout: float) -> None:
        super().__init__()
        if embedding_dim % num_heads != 0:
            raise ValueError("[ERROR] attention: embedding_dim must divide num_heads")

        self.num_heads = num_heads
        self.head_dim = embedding_dim // num_heads
        self.query = nn.Linear(embedding_dim, embedding_dim)
        self.key = nn.Linear(embedding_dim, embedding_dim)
        self.value = nn.Linear(embedding_dim, embedding_dim)
        self.output = nn.Linear(embedding_dim, embedding_dim)
        self.dropout = nn.Dropout(dropout)
        self.last_attention_weights: torch.Tensor | None = None

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        batch_size, sequence_length, embedding_dim = hidden.shape

        q = self.query(hidden)
        k = self.key(hidden)
        v = self.value(hidden)

        q = q.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        ).transpose(1, 2)
        k = k.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        ).transpose(1, 2)
        v = v.view(
            batch_size, sequence_length, self.num_heads, self.head_dim
        ).transpose(1, 2)

        scores = q @ k.transpose(-2, -1)
        scores = scores / math.sqrt(self.head_dim)

        mask = causal_mask(sequence_length, hidden.device)
        scores = scores.masked_fill(~mask, float("-inf"))

        attention_weights = F.softmax(scores, dim=-1)
        self.last_attention_weights = attention_weights.detach()

        context = self.dropout(attention_weights) @ v
        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(batch_size, sequence_length, embedding_dim)
        )
        return self.output(context)
