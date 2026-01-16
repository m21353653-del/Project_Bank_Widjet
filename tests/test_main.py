from unittest.mock import patch

from main import main

# фиктивные транзакции для теста
FAKE_TRANSACTIONS = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2026-01-16T12:00:00",
        "operationAmount": {"amount": "1000", "currency": {"name": "рубль", "code": "RUB"}},
        "description": "Оплата",
        "from": "1234 5678 9012 3456",
        "to": "6543 2109 8765 4321",
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2026-01-15T12:00:00",
        "operationAmount": {"amount": "500", "currency": {"name": "доллар", "code": "USD"}},
        "description": "Покупка",
        "from": "",
        "to": "1111 2222 3333 4444",
    },
]


# Подмена функций чтения файлов
@patch("main.read_transactions_from_csv", return_value=FAKE_TRANSACTIONS)
@patch("main.read_transactions_from_exel", return_value=FAKE_TRANSACTIONS)
@patch("main.get_transaction_data", return_value=FAKE_TRANSACTIONS)
def test_main_csv_flow(mock_json, mock_excel, mock_csv, capsys):
    user_inputs = iter(["2", "EXECUTED", "Нет", "Да", "Нет"])

    with patch("builtins.input", lambda _: next(user_inputs)):
        main()

    captured = capsys.readouterr()
    assert "Оплата" in captured.out
    assert "RUB" in captured.out
    assert "Покупка" not in captured.out


def test_sorting_descending(capsys):
    user_inputs = iter(["1", "EXECUTED", "Да", "ПО УБЫВАНИЮ", "Нет", "Нет"])

    fake_transactions = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2026-01-16T12:00:00",
            "operationAmount": {"amount": "100", "currency": {"name": "рубль", "code": "RUB"}},
            "description": "Оплата",
            "from": "1111 2222 3333 4444",
            "to": "5555 6666 7777 8888",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2026-01-15T12:00:00",
            "operationAmount": {"amount": "200", "currency": {"name": "рубль", "code": "RUB"}},
            "description": "Покупка",
            "from": "1111 2222 3333 4444",
            "to": "5555 6666 7777 8888",
        },
    ]

    with (
        patch("main.read_transactions_from_csv", return_value=fake_transactions),
        patch("main.read_transactions_from_exel", return_value=fake_transactions),
        patch("main.get_transaction_data", return_value=fake_transactions),
        patch("builtins.input", lambda _: next(user_inputs)),
    ):
        main()

    captured = capsys.readouterr()

    assert captured.out.index("Оплата") < captured.out.index("Покупка")
