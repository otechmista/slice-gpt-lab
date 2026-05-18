import pytest

from app.context import ContextMessage, build_chat_context, trim_context_to_length


def test_build_chat_context_adds_assistant_marker():
    context = build_chat_context(
        [ContextMessage(role="user", content="hi")],
        include_assistant_marker=True,
    )

    assert context.startswith("<|user|>\nhi")
    assert context.endswith("<|assistant|>\n")


def test_build_chat_context_rejects_unknown_role():
    with pytest.raises(ValueError, match="unsupported role"):
        build_chat_context(
            [ContextMessage(role="tool", content="pizza")],
            include_assistant_marker=True,
        )


def test_trim_context_to_length_keeps_latest_text():
    assert trim_context_to_length("abcdef", max_characters=3) == "def"
