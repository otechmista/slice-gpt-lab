"""Transformer block orchestration."""

from torch import nn

try:
    from .attention import MultiHeadCausalSelfAttention
    from .feedforward import FeedForward
except ImportError:  # pragma: no cover - supports `python app/train.py`
    from attention import MultiHeadCausalSelfAttention
    from feedforward import FeedForward


class TransformerBlock(nn.Module):
    """Attention plus feed-forward with residual connections."""

    def __init__(self, embedding_dim: int, num_heads: int, dropout: float) -> None:
        super().__init__()
        self.attention_norm = nn.LayerNorm(embedding_dim)
        self.attention = MultiHeadCausalSelfAttention(embedding_dim, num_heads, dropout)
        self.feedforward_norm = nn.LayerNorm(embedding_dim)
        self.feedforward = FeedForward(embedding_dim, dropout)

    def forward(self, hidden):
        # Residual connections keep the original signal available while each
        # sub-layer learns a useful adjustment.
        hidden = hidden + self.attention(self.attention_norm(hidden))
        hidden = hidden + self.feedforward(self.feedforward_norm(hidden))
        return hidden
