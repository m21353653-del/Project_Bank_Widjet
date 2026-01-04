from codecs import replace_errors

import pytest
from src.utils import get_transaction_data


def test_get_transaction_data():
    result = get_transaction_data("./data/operations.json")
    assert len(result) == 101
    assert result[0]["date"] == "2019-08-26T10:50:58.294041"


def test_get_transaction_data_no_empty():
    result = get_transaction_data("./data/test_json.json")
    assert len(result) == 0

    with pytest.raises(IndexError):
        assert result[0]["date"]


def test_get_transaction_no_file():
    result = get_transaction_data("./data/test.json")
    assert len(result) == 0
    assert result == []


def test_get_transaction_error():
    result = get_transaction_data("./data/test_2_json.json")
    assert len(result) == 0
    assert result == []


def test_get_transaction_no_key():
    result = get_transaction_data("./data/test_3_json.json")
    assert len(result) == 2

    with pytest.raises(TypeError):
        result["amount"]