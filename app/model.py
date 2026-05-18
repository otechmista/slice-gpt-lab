"""Main Mini GPT model."""

import torch
from torch import nn

try:
    from .block import TransformerBlock
    from .config import ModelConfig
    from .embedding import TokenEmbedding
    from .position import PositionalEmbedding
except ImportError:  # pragma: no cover - supports script execution
    from block import TransformerBlock
    from config import ModelConfig
    from embedding import TokenEmbedding
    from position import PositionalEmbedding


class MiniGPT(nn.Module):
    """Tiny GPT-like model for visible next-token prediction."""

    def __init__(self, vocab_size: int, config: ModelConfig) -> None:
        super().__init__()
        self.config = config
        self.token_embedding = TokenEmbedding(vocab_size, config.embedding_dim)
        self.position_embedding = PositionalEmbedding(
            config.block_size, config.embedding_dim
        )
        self.blocks = nn.ModuleList(
            [
                TransformerBlock(
                    config.embedding_dim,
                    config.num_heads,
                    config.dropout,
                )
                for _ in range(config.num_layers)
            ]
        )
        self.final_norm = nn.LayerNorm(config.embedding_dim)
        self.output = nn.Linear(config.embedding_dim, vocab_size)

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        if token_ids.ndim != 2:
            raise ValueError("[ERROR] model: token_ids must have shape [batch, time]")

        _, sequence_length = token_ids.shape
        if sequence_length > self.config.block_size:
            raise ValueError("[ERROR] model: sequence length exceeds block_size")

        hidden = self.token_embedding(token_ids)
        hidden = self.position_embedding(hidden)
        for block in self.blocks:
            hidden = block(hidden)
        hidden = self.final_norm(hidden)
        return self.output(hidden)
