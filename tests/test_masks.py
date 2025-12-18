import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number():
    assert get_mask_card_number("2200213467788976") == "2200 21** **** 8976"


@pytest.mark.parametrize(
    "number, result",
    [
        ("220021346778897", "Номер карты должен быть равен 16!"),
        ("22001234567898765", "Номер карты должен быть равен 16!"),
        ("", "Номер карты должен быть равен 16!"),
    ],
)
def test_length_card_number(number, result):
    assert get_mask_card_number(number) == result


def test_empty_card_number():
    with pytest.raises(TypeError):
        get_mask_card_number()


# Тесты функции get_mask_account
def test_mask_account():
    assert get_mask_account("23768976567898234567") == "**4567"


@pytest.mark.parametrize("number, result", [("234567894567234678914", "**8914"), ("9856345682359854278", "**4278")])
def test_length_mask_account(number, result):
    assert get_mask_account(number) == result


@pytest.mark.parametrize("number, result", [("", "**"), ("232", "**232"), ("1234", "**1234")])
def test_min_length_mask_account(number, result):
    assert get_mask_account(number) == result
