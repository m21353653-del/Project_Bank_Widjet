import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", 'w', encoding="utf-8")
stream_handler = logging.StreamHandler()
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску, в формате XXXX XX** **** XXXX"""
    digits_card_number = []
    number_counter = 0

    # Длина номера карты должна быть == 16
    logger.debug("Проверяем длинну номера карты...")
    if len(number_card) < 16 or len(number_card) > 16:
        logger.error("Номер карты должен быть равен 16!")
        return "Номер карты должен быть равен 16!"

    logger.debug("Проверка длины номера карты пройдена успешно!")
    logger.debug("Начинаем маскировку...")
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
    logger.debug("Успешно!")
    return formatted_card_number


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску, в формате **XXXX"""
    logger.debug("Принимаю номер счета...")
    digits_account_number = [num for num in number_account[-4:]]
    logger.debug("Начинаю маскировку...")
    mask_account_number = "**" + "".join(digits_account_number)
    logger.debug("Успешно!")
    return mask_account_number
