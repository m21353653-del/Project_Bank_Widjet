import pandas as pd


def clean_dict(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        if isinstance(v, dict):
            nested = clean_dict(v)
            if nested:
                new_d[k] = nested
        elif v not in ("", 0):
            new_d[k] = v
    return new_d


def read_transactions_from_csv(file: str) -> list:
    """Принимает файл сsv и возвращает список словарей с транзакциями"""
    transactions = []

    try:
        df = pd.read_csv(file, sep=";")

        for _, row in df.iterrows():
            transaction = {
                "id": int(row["id"] if not pd.isna(row["id"]) else 0),
                "state": str(row["state"] if not pd.isna(row["state"]) else ""),
                "date": str(row["date"] if not pd.isna(row["date"]) else ""),
                "operationAmount": {
                    "amount": str(row["amount"] if not pd.isna(row["amount"]) else ""),
                    "currency": {
                        "name": str(row["currency_name"] if not pd.isna(row["currency_name"]) else ""),
                        "code": str(row["currency_code"] if not pd.isna(row["currency_code"]) else ""),
                    },
                },
                "description": str(row["description"] if not pd.isna(row["description"]) else ""),
                "from": str(row["from"] if not pd.isna(row["from"]) else ""),
                "to": str(row["to"] if not pd.isna(row["to"]) else ""),
            }

            transaction = clean_dict(transaction)

            transactions.append(transaction)

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
            transaction = {
                "id": int(row["id"] if not pd.isna(row["id"]) else 0),
                "state": str(row["state"] if not pd.isna(row["state"]) else ""),
                "date": str(row["date"] if not pd.isna(row["date"]) else ""),
                "operationAmount": {
                    "amount": str(row["amount"] if not pd.isna(row["amount"]) else ""),
                    "currency": {
                        "name": str(row["currency_name"] if not pd.isna(row["currency_name"]) else ""),
                        "code": str(row["currency_code"] if not pd.isna(row["currency_code"]) else ""),
                    },
                },
                "description": str(row["description"] if not pd.isna(row["description"]) else ""),
                "from": str(row["from"] if not pd.isna(row["from"]) else ""),
                "to": str(row["to"] if not pd.isna(row["to"]) else ""),
            }

            transaction = clean_dict(transaction)

            transactions.append(transaction)

        return transactions
    except FileNotFoundError:
        print(f"Файл: {file} не найден! Проверить, правильно ли указан путь и попробуйте снова.")
        return transactions


read_transactions_from_csv("../data/transactions.csv")
