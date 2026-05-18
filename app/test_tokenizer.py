import pytest

from app.tokenizer import CharacterTokenizer


def test_tokenizer_encode_decode_roundtrip():
    tokenizer = CharacterTokenizer.from_text("pizza")

    token_ids = tokenizer.encode("pizza")

    assert tokenizer.decode(token_ids) == "pizza"


def test_invalid_token_rejected():
    tokenizer = CharacterTokenizer.from_text("abc")

    with pytest.raises(ValueError, match="unsupported token"):
        tokenizer.encode("z")


def test_invalid_token_id_rejected():
    tokenizer = CharacterTokenizer.from_text("abc")

    with pytest.raises(ValueError, match="token id 9999"):
        tokenizer.decode([9999])
