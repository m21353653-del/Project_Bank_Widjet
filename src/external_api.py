import os

import requests
from dotenv import load_dotenv

from src.utils import get_transaction_data

# Загрузка переменных из .env-файла
load_dotenv()

headers = {"apikey": os.getenv("API_KEY")}


def get_transaction_amount(transactions: list[dict]) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму в рублях,
    если сумма в EUR or USD, делается запрос к внешнему API для конвертации в рубли"""
    amount = 0.0

    for trans in transactions:
        try:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                amount += float(trans["operationAmount"]["amount"])
            else:
                code = trans["operationAmount"]["currency"]["code"]
                count = trans["operationAmount"]["amount"]

                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={count}"
                response = requests.get(url, headers=headers, data={})
                response = response.json()

                amount += float(response["result"])
        except KeyError:
            continue

    return amount
