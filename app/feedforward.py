"""Feed-forward network used inside transformer blocks."""

from torch import nn


class FeedForward(nn.Module):
    """Small MLP applied independently to each token position."""

    def __init__(self, embedding_dim: int, dropout: float) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(embedding_dim, 4 * embedding_dim),
            nn.GELU(),
            nn.Linear(4 * embedding_dim, embedding_dim),
            nn.Dropout(dropout),
        )

    def forward(self, hidden):
        return self.network(hidden)
