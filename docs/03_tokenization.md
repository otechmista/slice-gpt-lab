# Tokenization

Tokenization converts text into numbers.

Neural networks do not read strings directly. They receive tensors. The tokenizer is the bridge between human text and numerical model input.

## File

```txt
app/tokenizer.py
```

## How This Project Tokenizes

This project uses a character-level tokenizer. Every unique character in `app/dataset.txt` receives an integer id.

Example:

```txt
text: pizza
ids:  [p_id, i_id, z_id, z_id, a_id]
```

The exact ids depend on the sorted vocabulary built from the dataset.

## Important Functions

- `CharacterTokenizer.from_text(text)`: builds the vocabulary.
- `encode(text)`: turns text into token ids.
- `decode(token_ids)`: turns token ids back into text.
- `to_dict()`: serializes the vocabulary into checkpoint metadata.
- `from_dict(data)`: restores the tokenizer from checkpoint metadata.

## Why Unsupported Characters Fail

If a prompt contains a character that was not in the training dataset, the tokenizer cannot encode it.

That is why the dataset language matters. The current project keeps public data and answers in English to keep the character vocabulary predictable.

## Relation to Real GPT Models

Real GPT-style systems usually use subword tokenizers. They can represent many words with fewer tokens. Character tokenization is less realistic, but much easier to understand.
