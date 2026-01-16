from unittest.mock import patch

import pandas as pd

from src.reading_different_formats import read_transactions_from_csv, read_transactions_from_exel


def test_read_transactions_from_csv():
    fake_df = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2026-01-16T12:00:00",
                "amount": 100,
                "currency_name": "рубль",
                "currency_code": "RUB",
                "description": "food",
                "from": "1111 2222 3333 4444",
                "to": "5555 6666 7777 8888",
            }
        ]
    )

    with patch("src.reading_different_formats.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = fake_df

        result = read_transactions_from_csv("fake_file.csv")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2026-01-16T12:00:00",
            "operationAmount": {"amount": "100", "currency": {"name": "рубль", "code": "RUB"}},
            "description": "food",
            "from": "1111 2222 3333 4444",
            "to": "5555 6666 7777 8888",
        }
    ]


def test_read_transactions_from_csv_file_not_found():
    result = read_transactions_from_csv("no_such_file.csv")
    assert result == []


def test_read_transactions_from_excel():
    fake_df = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2026-01-16T12:00:00",
                "amount": 100,
                "currency_name": "рубль",
                "currency_code": "RUB",
                "description": "food",
                "from": "1111 2222 3333 4444",
                "to": "5555 6666 7777 8888",
            }
        ]
    )

    with patch("src.reading_different_formats.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = fake_df

        result = read_transactions_from_exel("fake_file.xlsx")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2026-01-16T12:00:00",
            "operationAmount": {"amount": "100", "currency": {"name": "рубль", "code": "RUB"}},
            "description": "food",
            "from": "1111 2222 3333 4444",
            "to": "5555 6666 7777 8888",
        }
    ]
