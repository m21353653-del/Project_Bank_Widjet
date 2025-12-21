from hmac import trans_36
from typing import Iterable


def filter_by_currency(list_dict: list, val: str) -> Iterable[dict]:
    ''' Принимает список словарей с транзакциями и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной '''

    for trans in list_dict:
        if trans["operationAmount"]["currency"]["code"] == val:
            yield trans


def transaction_descriptions(list_dict: list, start=0) -> str:
    ''' принимает список словарей с транзакциями и возвращает описание каждой операции по очереди '''
    while True:
        yield list_dict[start]["description"]
        start += 1

def card_number_generator(start: int, stop: int) -> str:
    ''' Генератор принимает начальное и конечное значения для генерации диапазона номеров. '''
    for num in range(start, stop):
        number_card = f"{num:016d}"
        formatted = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:16]}"
        yield formatted