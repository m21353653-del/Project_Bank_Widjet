def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску, в формате XXXX XX** **** XXXX"""
    digits_card_number = []
    number_counter = 0

    # Длина номера карты должна быть == 16
    if len(number_card) < 16 or len(number_card) > 16:
        return "Номер карты должен быть равен 16!"

    for i in range(len(number_card)):
        # Проверяем если индекс чисел от 6-11, тогда делаем замену на *
        if 6 <= i <= 11:
            number_counter += 1
            digits_card_number.append("*")
        else:
            number_counter += 1
            digits_card_number.append(number_card[i])

        if number_counter == 4:
            number_counter = 0
            digits_card_number.append(" ")

    formatted_card_number = "".join(digits_card_number).strip()
    return formatted_card_number


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в формате **XXXX"""
    digits_account_number = [num for num in number_account[-4:]]
    mask_account_number = "**" + "".join(digits_account_number)
    return mask_account_number
