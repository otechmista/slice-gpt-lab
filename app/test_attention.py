import torch

from app.attention import causal_mask


def test_causal_mask_blocks_future_tokens():
    mask = causal_mask(4)

    expected = torch.tensor(
        [
            [True, False, False, False],
            [True, True, False, False],
            [True, True, True, False],
            [True, True, True, True],
        ]
    )
    assert torch.equal(mask.cpu(), expected)
