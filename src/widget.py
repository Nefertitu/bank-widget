import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_widget(card_or_account_number: str) -> str:
    """Функция обрабатывает полученные данные о карте/счете и возвращает замаскированный номер"""

    if len(card_or_account_number) > 0:
        number_for_mask = ""
        name_mask = ""
        for i in card_or_account_number:
            if i.isdigit() is True:
                number_for_mask += i
                # print(number_for_mask)
            else:
                name_mask += i
                # print(name_mask)

        if number_for_mask != 0 and name_mask != 0:

            if len(number_for_mask) == 20 and re.findall(r"\b[Сс]ч[е|ё]т\b\s", name_mask) is not None:
                result = get_mask_account(number_for_mask)
                total_result = name_mask + result
                return total_result

            elif 13 <= len(number_for_mask) <= 19 and len(number_for_mask) != 14 and len(number_for_mask) != 17 and number_for_mask.isdigit() is True:
                result = get_mask_card_number(number_for_mask)
                total_result = name_mask + result
                return total_result

            else:
                return "введены некорректные данные"

    else:
        return "пустой ввод"


# print (mask_account_widget(""))
def get_date(formatted_date: str) -> str:
    """Функция преобразует полученную строку с датой в дату формата 'ДД.ММ.ГГГГ'"""
    received_date = datetime.strptime(formatted_date[:10], "%Y-%m-%d")
    required_date = received_date.strftime("%d.%m.%Y")
    return required_date
