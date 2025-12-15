def filter_by_state(my_list: list, state: str = "EXECUTED") -> list:
    ''' Функцция возвращает список словарей,
    если значение state в словаре = "EXECUTED"
    Возвращает new_list с значение state в словаре = "EXECUTED" '''
    new_list = []

    for item in my_list:
        if item["state"] == state:
            new_list.append(item)

    return new_list
