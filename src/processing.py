import re


def filter_by_state(my_list: list, state: str = "EXECUTED") -> list:
    """Функцция возвращает список словарей,
    если значение state в словаре = "EXECUTED"
    Возвращает new_list с значение state в словаре = "EXECUTED" """
    new_list_formated = []

    for item in my_list:
        if item["state"] == state:
            new_list_formated.append(item)

    return new_list_formated


def sort_by_date(my_list: list, is_reverse: bool = True) -> list:
    """Функция принимает список словарей
    и необязательный параметр - метод сортировки
    Возвращает новый список словарей сортированый по дате"""
    list_date_sorted = sorted(my_list, key=lambda date: date["date"], reverse=is_reverse)
    return list_date_sorted


def process_bank_search(data:list[dict], search:str)->list[dict]:
    ''' Принимает список словарей с данными о банковских операциях - data
     и строку поиска - search, возвращает список словарей, у которых в описании есть search. '''
    new_list = []

    try:
        for my_dict in data:
            descriptions = my_dict["description"]
            match = re.search(search, descriptions)
            if match:
                new_list.append(my_dict)
    except TypeError:
        print("Произошла ошибка, проверьте входные данные... Мы получили не то, что ожидали.")

    return new_list
