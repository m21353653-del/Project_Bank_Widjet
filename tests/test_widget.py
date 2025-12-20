import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "line, result",
    [("Счет 23567898653092468198", "Счет **8198"), ("MasterCard 2200876587652343", "MasterCard 2200 87** **** 2343")],
)
def test_type_recognition_mask_account_card(line, result):
    assert mask_account_card(line) == result


@pytest.mark.parametrize(
    "line, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_universality_mask_account_card(line, result):
    assert mask_account_card(line) == result


def test_error_mask_account_card():
    with pytest.raises(TypeError):
        mask_account_card()


# get_date
def test_get_date(my_date):
    assert get_date("2024-03-11T02:26:18.671407") == my_date


@pytest.mark.parametrize(
    "line, result",
    [
        ("2024-03-11T02:26:18.67140", "11.03.2024"),
        ("2024-03-11T02:26:18.6714042", "11.03.2024"),
        ("25-3-11T2:26:18.671404", "11.3.25"),
    ],
)
def test_length_get_date(line, result):
    assert get_date(line) == result


def test_empty_get_date():
    with pytest.raises(IndexError):
        get_date("")
        get_date("fggfdgd")

    with pytest.raises(TypeError):
        get_date()
