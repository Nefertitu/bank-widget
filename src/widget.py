from src.masks import get_mask_account, get_mask_card_number


def mask_account_widget(card_or_account_number: str) -> str:
    """Функция обрабатывает полученные данные о карте/счете и возвращает замаскированный номер"""
    number_for_mask = ""
    name_mask = ""
    for i in card_or_account_number:
        if i.isdigit() is True:
            number_for_mask += i
        else:
            name_mask += i

    if len(number_for_mask) == 16:
        result = get_mask_card_number(number_for_mask)
        total_result = name_mask + result
    else:
        result = get_mask_account(number_for_mask)
        total_result = name_mask + result

    return total_result
