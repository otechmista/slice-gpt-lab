"""Autoregressive inference entrypoint."""

import argparse
import warnings
from pathlib import Path

warnings.filterwarnings(
    "ignore",
    message="Failed to initialize NumPy:*",
    category=UserWarning,
)

try:
    from .checkpoint import load_checkpoint
    from .context import ContextMessage, build_chat_context
    from .config import DEFAULT_CHECKPOINT_PATH
    from .logging_utils import log_info
    from .sampling import choose_next_token
except ImportError:  # pragma: no cover - supports `python app/infer.py`
    from checkpoint import load_checkpoint
    from context import ContextMessage, build_chat_context
    from config import DEFAULT_CHECKPOINT_PATH
    from logging_utils import log_info
    from sampling import choose_next_token


def format_chat_prompt(prompt: str) -> str:
    """Format user text as the conversation pattern seen during training."""

    stripped = prompt.strip()
    if "<|assistant|>" in stripped.lower():
        return stripped
    if "<|user|>" in stripped.lower():
        return f"{stripped}\n<|assistant|>\n"
    return build_chat_context(
        [ContextMessage(role="user", content=stripped)],
        include_assistant_marker=True,
    )


def extract_assistant_answer(generated_text: str) -> str:
    """Extract only the assistant response from generated conversation text."""

    marker = "<|assistant|>"
    lower_text = generated_text.lower()
    marker_index = lower_text.rfind(marker)
    if marker_index == -1:
        return generated_text.strip()

    answer = generated_text[marker_index + len(marker) :]
    for stop_marker in ("<|end|>", "<|user|>", "<|system|>"):
        stop_index = answer.lower().find(stop_marker)
        if stop_index != -1:
            answer = answer[:stop_index]
    return answer.strip()


def sanitize_for_tokenizer(text: str, vocabulary: set[str]) -> str:
    """Replace unsupported prompt characters before character-level encoding."""

    fallback = " " if " " in vocabulary else next(iter(vocabulary))
    return "".join(
        character if character in vocabulary else fallback for character in text
    )


def generate_text(
    prompt: str,
    checkpoint_path: Path = DEFAULT_CHECKPOINT_PATH,
    max_tokens: int = 80,
    temperature: float = 0.05,
    seed: int = 1337,
    verbose: bool = False,
) -> str:
    """Generate an answer using only the trained model checkpoint."""

    if not prompt.strip():
        raise ValueError("[ERROR] infer: prompt cannot be empty")

    conversation = format_chat_prompt(prompt)
    generated = generate_model_text(
        conversation,
        checkpoint_path=checkpoint_path,
        max_tokens=max_tokens,
        temperature=temperature,
        seed=seed,
        verbose=verbose,
    )
    return extract_assistant_answer(generated)


def generate_model_text(
    prompt: str,
    checkpoint_path: Path = DEFAULT_CHECKPOINT_PATH,
    max_tokens: int = 80,
    temperature: float = 0.05,
    seed: int = 1337,
    verbose: bool = False,
) -> str:
    """Generate raw text from the tiny trained model."""

    import torch

    if not prompt:
        raise ValueError("[ERROR] infer: prompt cannot be empty")
    if max_tokens <= 0:
        raise ValueError("[ERROR] infer: max_tokens must be positive")

    torch.manual_seed(seed)
    model, tokenizer, config = load_checkpoint(checkpoint_path)
    prompt = sanitize_for_tokenizer(prompt, set(tokenizer.vocabulary.stoi))
    generated = tokenizer.encode(prompt)

    model.eval()
    with torch.no_grad():
        for step in range(max_tokens):
            context = generated[-config.block_size :]
            inputs = torch.tensor([context], dtype=torch.long)
            logits = model(inputs)
            next_logits = logits[0, -1, :]
            next_token_id = choose_next_token(next_logits, temperature)
            generated.append(next_token_id)
            if verbose:
                log_info(
                    "infer", f"generation step={step + 1} token_id={next_token_id}"
                )

            text = tokenizer.decode(generated)
            if "<|end|>" in text.lower().split("<|assistant|>", maxsplit=1)[-1]:
                break

    return tokenizer.decode(generated)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", default="What pizza do you recommend?")
    parser.add_argument("--max-tokens", type=int, default=80)
    parser.add_argument("--temperature", type=float, default=0.05)
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT_PATH)
    parser.add_argument("--raw-model", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if args.raw_model:
        print(
            generate_model_text(
                prompt=format_chat_prompt(args.prompt),
                checkpoint_path=args.checkpoint,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
                verbose=args.verbose,
            )
        )
    else:
        print(
            generate_text(
                prompt=args.prompt,
                checkpoint_path=args.checkpoint,
                max_tokens=args.max_tokens,
                temperature=args.temperature,
                verbose=args.verbose,
            )
        )


if __name__ == "__main__":
    main()
