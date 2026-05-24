from app.config import DEFAULT_DATASET_PATH
from app.dataset import load_dataset


def test_delivery_examples_do_not_conflict_with_defined_delivery_fact():
    text = load_dataset(DEFAULT_DATASET_PATH)

    assert "Slice Pizza offers local delivery" in text
    assert (
        "Assistant: Delivery details are not defined for this fictional pizzeria."
        not in text
    )


def test_dataset_reinforces_common_drink_and_meat_questions():
    text = load_dataset(DEFAULT_DATASET_PATH)

    assert "Customer: do you have coca coca" in text
    assert "Coca Coca, treat it as a typo for Coca-Cola or Coke" in text
    assert "Customer: does portuguese have more meat" in text
    assert "Pepperoni is the meatier option" in text
