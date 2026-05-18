"""Character-level tokenizer and vocabulary mapping."""

from dataclasses import dataclass

TokenId = int


@dataclass(frozen=True)
class Vocabulary:
    stoi: dict[str, TokenId]
    itos: dict[TokenId, str]

    @property
    def size(self) -> int:
        return len(self.stoi)

    def to_dict(self) -> dict[str, dict[str, str | int]]:
        return {
            "stoi": self.stoi,
            "itos": {str(token_id): token for token_id, token in self.itos.items()},
        }

    @classmethod
    def from_dict(cls, data: dict[str, dict[str, str | int]]) -> "Vocabulary":
        stoi = {str(token): int(token_id) for token, token_id in data["stoi"].items()}
        itos = {int(token_id): str(token) for token_id, token in data["itos"].items()}
        return cls(stoi=stoi, itos=itos)


class CharacterTokenizer:
    """One-character-one-token tokenizer.

    This is less powerful than BPE tokenizers used by GPT-like production
    systems, but it makes every vocabulary decision visible while studying.
    """

    def __init__(self, vocabulary: Vocabulary) -> None:
        self.vocabulary = vocabulary

    @property
    def vocab_size(self) -> int:
        return self.vocabulary.size

    @classmethod
    def from_text(cls, text: str) -> "CharacterTokenizer":
        if not text:
            raise ValueError(
                "[ERROR] tokenizer: cannot build vocabulary from empty text"
            )

        tokens = sorted(set(text))
        stoi = {token: token_id for token_id, token in enumerate(tokens)}
        itos = {token_id: token for token, token_id in stoi.items()}
        return cls(Vocabulary(stoi=stoi, itos=itos))

    def encode(self, text: str) -> list[TokenId]:
        token_ids: list[TokenId] = []
        for token in text:
            if token not in self.vocabulary.stoi:
                raise ValueError(f"[ERROR] tokenizer: unsupported token {token!r}")
            token_ids.append(self.vocabulary.stoi[token])
        return token_ids

    def decode(self, token_ids: list[TokenId]) -> str:
        tokens: list[str] = []
        for token_id in token_ids:
            if token_id not in self.vocabulary.itos:
                raise ValueError(
                    f"[ERROR] tokenizer: token id {token_id} does not exist in vocabulary"
                )
            tokens.append(self.vocabulary.itos[token_id])
        return "".join(tokens)

    def to_dict(self) -> dict[str, dict[str, str | int]]:
        return self.vocabulary.to_dict()

    @classmethod
    def from_dict(cls, data: dict[str, dict[str, str | int]]) -> "CharacterTokenizer":
        return cls(Vocabulary.from_dict(data))
