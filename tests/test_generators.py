import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(my_list):
    generation = filter_by_currency(my_list, "USD")

    assert next(generation) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(generation) == {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }


def test_filter_no_transactions(my_list):
    with pytest.raises(StopIteration):
        generation = filter_by_currency(my_list, "RUB")
        assert next(generation)

        generation = filter_by_currency([], "USD")
        assert next(generation)


# transaction_descriptions
def test_