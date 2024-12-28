import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """
    Функция обрабатывает полученные данные о карте/счете и возвращает замаскированный номер
    :param card_or_account_number:
    :return:
    """

    if type(card_or_account_number) is str:

        if len(card_or_account_number) > 0:
            number_for_mask = ""
            name_mask = ""
            for i in card_or_account_number:
                if i.isdigit() is True:
                    number_for_mask += i
                else:
                    name_mask += i

            if number_for_mask != "" and name_mask != "":

                if len(number_for_mask) == 20 and re.findall(r"\b[Сс]ч[е|ё]т\b\s", name_mask) is not None:
                    result = get_mask_account(number_for_mask)
                    total_result = name_mask + result
                    return total_result

                elif (
                    13 <= len(number_for_mask) <= 19
                    and len(number_for_mask) != 14
                    and len(number_for_mask) != 17
                    and number_for_mask.isdigit() is True
                ):
                    result = get_mask_card_number(number_for_mask)
                    total_result = name_mask + result
                    return total_result

                return "некорректный ввод данных"

            return "некорректный ввод данных"

        return "пустой ввод"
    else:
        raise TypeError("получен аргумент некорректного типа")

    # except TypeError as e:
    #   return f"TypeError: {e}"


def get_data(formatted_date: str | None) -> str:
    """
    Функция преобразует полученную строку с датой в дату формата 'ДД.ММ.ГГГГ'
    :param formatted_date:
    :return:
    """
    if formatted_date:
        received_date = re.search(r".*(\d{4}).(\d{2}).(\d{2}).*", formatted_date)
        result = f"{received_date.group(3)}.{received_date.group(2)}.{received_date.group(1)}"
        return result

    return "пустой ввод"
