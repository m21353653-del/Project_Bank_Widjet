from unittest.mock import Mock, patch

from src.external_api import get_transaction_amount

# Тестовые данные
VALID_RUB_TRANS = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}

VALID_USD_TRANS = {"operationAmount": {"amount": "2.00", "currency": {"code": "USD"}}}

INVALID_TRANS_MISSING_AMOUNT = {"operationAmount": {"currency": {"code": "USD"}}}

EMPTY_TRANS = {}

# Мок-ответ API: 2 USD → 180 RUB (курс 90)
MOCK_API_RESPONSE = {"result": 180.00}


def test_rub_only():
    transactions = [VALID_RUB_TRANS, VALID_RUB_TRANS]
    amount = get_transaction_amount(transactions)
    assert amount == 201.00  # 100.50 + 100.50


@patch("requests.get")
def test_usd_conversion(mock_get):
    mock_get.return_value = Mock(status_code=200, json=lambda: MOCK_API_RESPONSE)

    transactions = [VALID_USD_TRANS]
    amount = get_transaction_amount(transactions)
    assert amount == 180.00


def test_empty_transactions():
    amount = get_transaction_amount([])
    assert amount == 0.0


def test_invalid_transaction_missing_amount():
    transactions = [INVALID_TRANS_MISSING_AMOUNT]
    amount = get_transaction_amount(transactions)
    assert amount == 0.0


def test_invalid_empty_transaction():
    transactions = [EMPTY_TRANS]
    amount = get_transaction_amount(transactions)
    assert amount == 0.0
