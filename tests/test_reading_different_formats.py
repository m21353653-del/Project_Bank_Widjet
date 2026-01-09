from unittest.mock import patch
import pandas as pd
from src.reading_different_formats import read_transactions_from_csv, read_transactions_from_exel

def test_read_transactions_from_csv():
    fake_df = pd.DataFrame([
        {"id": 1, "amount": 100, "category": "food"},
        {"id": 2, "amount": 200, "category": "taxi"},
    ])

    with patch("src.reading_different_formats.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = fake_df

        result = read_transactions_from_csv("fake_file.csv")

    assert result == [
        {"id": 1, "amount": 100, "category": "food"},
        {"id": 2, "amount": 200, "category": "taxi"},
    ]


def test_read_transactions_from_excel():
    fake_df = pd.DataFrame([
        {"id": 10, "amount": 999, "category": "test"},
    ])

    with patch("src.reading_different_formats.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = fake_df

        result = read_transactions_from_exel("fake_file.xlsx")

    assert result == [
        {"id": 10, "amount": 999, "category": "test"},
    ]
