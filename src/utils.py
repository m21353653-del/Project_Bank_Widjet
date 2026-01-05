import json
from typing import Any
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", 'w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transaction_data(json_file: str) -> Any:
    """Функция принимает json файл и возвращает список словарей с даными об операциях"""
    list_operations = []
    logger.debug(f"json_file: Готов к отрытию.")
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            list_operations = json.load(file)
            logger.debug(f"json_file: Успешно открыт.")
            logger.debug(f"Делаем магию...")

        logger.debug(f"Успешно.")
        return list_operations
    except FileNotFoundError:
        logger.error('Данный файл не найден! Возвращаем пустой список.')
        return list_operations
    except json.JSONDecodeError:
        logger.error('Формат файла не является JSON-объектом! Возвращаем пустой список.')
        return list_operations
    except TypeError:
        logger.error('Увы! Но там не то, что мы ожидали!')
        return list_operations
