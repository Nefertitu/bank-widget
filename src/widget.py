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
            n_f_m = ""
            name_mask = ""
            for i in card_or_account_number:
                if i.isdigit() is True:
                    n_f_m += i
                else:
                    name_mask += i

            if n_f_m != "" and name_mask != "":

                if len(n_f_m) == 20 and re.findall(r"\b[Сс]ч[е|ё]т\b\s", name_mask) is not None:
                    result = get_mask_account(n_f_m)
                    total_result = name_mask + result
                    return total_result

                elif 13 <= len(n_f_m) <= 19 and len(n_f_m) != 14 and len(n_f_m) != 17 and n_f_m.isdigit() is True:
                    result = get_mask_card_number(n_f_m)
                    total_result = name_mask + result
                    return total_result

                return "некорректный ввод данных"

            return "некорректный ввод данных"

        return "пустой ввод"
    else:
        raise TypeError("получен аргумент некорректного типа")

    # except TypeError as e:
    #   return f"TypeError: {e}"


def get_data(formatted_date: str | None) -> str | None:
    """
    Функция преобразует полученную строку с датой в дату формата 'ДД.ММ.ГГГГ'
    :param formatted_date:
    :return:
    """
    if formatted_date:
        received_date = re.search(r".*(\d{4}).(\d{2}).(\d{2}).*", formatted_date)

        if received_date is not None:
            result = f"{received_date.group(3)}.{received_date.group(2)}.{received_date.group(1)}"
        else:
            result = ""
        return result

    return "пустой ввод"
