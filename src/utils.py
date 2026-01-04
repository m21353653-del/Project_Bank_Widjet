import json
from typing import Any


def get_transaction_data(json_file: str) -> Any:
    """Функция принимает json файл и возвращает список словарей с даными об операциях"""
    list_operations = []

    try:
        with open(json_file, "r", encoding="utf-8") as file:
            list_operations = json.load(file)

        return list_operations
    except FileNotFoundError:
        return list_operations
    except json.JSONDecodeError:
        return list_operations
    except TypeError:
        return list_operations
