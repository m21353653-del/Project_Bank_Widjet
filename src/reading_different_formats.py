import pandas as pd


def read_transactions_from_csv(file: str) -> list:
    """Принимает файл сsv и возвращает список словарей с транзакциями"""
    transactions = []

    try:
        df = pd.read_csv(file, sep=";")

        for index, row in df.iterrows():
            transactions.append(dict(row))

        return transactions
    except FileNotFoundError:
        print(f"Файл: {file} не найден! Проверить, правильно ли указан путь и попробуйте снова.")
        return transactions


def read_transactions_from_exel(file: str) -> list:
    """Принимает файл сsv и возвращает список словарей с транзакциями"""
    transactions = []

    try:
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            transactions.append(dict(row))

        return transactions
    except FileNotFoundError:
        print(f"Файл: {file} не найден! Проверить, правильно ли указан путь и попробуйте снова.")
        return transactions
