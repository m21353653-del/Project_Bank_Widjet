def filter_by_state(my_list: list, state: str = "EXECUTED") -> list:
    ''' Функцция возвращает список словарей,
    если значение state в словаре = "EXECUTED"
    Возвращает new_list с значение state в словаре = "EXECUTED" '''
    new_list = []

    for item in my_list:
        if item["state"] == state:
            new_list.append(item)

    return new_list


def sort_by_date(my_list: list, is_reverse: bool = True) -> list:
    ''' Функция принимает список словарей
     и необязательный параметр - метод сортировки
     Возвращает новый список словарей сортированый по дате'''
    list_date_sorted = sorted(my_list, key=lambda date: date["date"], reverse=is_reverse)
    return list_date_sorted
