from src.masks import get_mask_account, get_mask_card_number  # type: ignore


def mask_account_card(card: str) -> str:
    """Функция принимает тип и номер карты/счета и возвращает строку с замаскированым номером"""
    if "Счет" in card:
        account_number = card[-20:]
        return card.replace(account_number, get_mask_account(account_number))
    else:
        number_card = card[-16:]
        return card.replace(number_card, get_mask_card_number(number_card))


def get_date(date: str) -> str:
    '''Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    new_date = date.split("T")[0]
    # Создаем список из чисел 2024, 03, 11, которые берем из new_date
    list_number = [num for num in new_date.split("-")]

    return f"{list_number[2]}.{list_number[1]}.{list_number[0]}"
