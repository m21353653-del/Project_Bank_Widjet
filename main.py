from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.reading_different_formats import read_transactions_from_csv, read_transactions_from_exel
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card


def main():
    """Запускает работу программы, представляет функциональность"""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_answer_menu = input("Пользователь: ")

    if user_answer_menu.strip() == "2":
        list_transactions = read_transactions_from_csv("./data/transactions.csv")
    elif user_answer_menu.strip() == "3":
        list_transactions = read_transactions_from_exel("./data/transactions_excel.xlsx")
    elif user_answer_menu.strip() == "1":
        list_transactions = get_transaction_data("./data/operations.json")

    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        user_filter_status = input("Пользователь: ")

        if user_filter_status.upper().strip() in ["EXECUTED", "CANCELED", "PENDING"]:
            list_result_filter = filter_by_state(list_transactions, user_filter_status.upper())
            print(f'Программа: Операции отфильтрованы по статусу "{user_filter_status.upper()}"')
            break
        print(f'Программа: Статус операции "{user_filter_status}" недоступен.')

    print("Программа: Отсортировать операции по дате? Да/Нет")
    user_answer_sorted_date = input("Пользователь: ").upper()

    if user_answer_sorted_date == "ДА":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        user_answer_sorted_direction = input("Пользователь: ").upper()

        if user_answer_sorted_direction.strip() == "ПО ВОЗРАСТАНИЮ":
            list_result_filter = sort_by_date(list_result_filter, False)
        elif user_answer_sorted_direction.strip() == "ПО УБЫВАНИЮ":
            list_result_filter = sort_by_date(list_result_filter)

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    user_answer_only_rub = input("Пользователь: ").upper()

    if user_answer_only_rub.strip() == "ДА":
        list_result_filter = list(filter_by_currency(list_result_filter, "RUB"))

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_answer_filter_word = input("Пользователь: ").upper()

    if user_answer_filter_word.strip() == "ДА":
        search = input("Программа: Введите строку по которой будет осущетсвляться поиск\nПользователь: ")
        list_result_filter = process_bank_search(list_result_filter, search)

    if len(list_result_filter) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Программа: Распечатываю итоговый список транзакций...")

    print(f"Программа:\n Всего банковских операций в выборке: {len(list_result_filter)}")

    for d in list_result_filter:
        print(get_date(d["date"]), d["description"])

        if "from" not in d:
            print(f"{mask_account_card(d["to"])}")
        else:
            print(f"{mask_account_card(d["from"])} -> {mask_account_card(d["to"])}")

        print(f"Сумма: {d["operationAmount"]["amount"]} {d["operationAmount"]['currency']["code"]}")
        print()


if __name__ == "__main__":
    main()
