import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("data, exp", [("12345678901234567890", "**7890"),
 ("12345123451234512345", "**2345"),
 ("12345678900987654321", "**4321")])
def test_get_mask_account(data: str, exp: str) -> None:
    assert get_mask_account(data) == exp

def test_get_mask_acc(dat: str, expec: str) -> None:
    assert get_mask_account(dat) == expec


@pytest.mark.parametrize("number_card, mask_card", [
    ("1234567891234567", "1234 56** **** 4567"),
    ("0987654321098765", "0987 65** **** 8765"),
    ("6574837462530293", "6574 83** **** 0293"),
])
def test_get_mask_card_number(number_card: str, mask_card: str) -> None:
    assert get_mask_card_number(number_card) == mask_card