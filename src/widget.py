import re
from typing import SupportsIndex, Any


def mask_account_card(card_or_account_number: SupportsIndex | slice) -> str:
    """
    Функция обрабатывает полученные данные о карте/счете и возвращает замаскированный номер
    :param card_or_account_number:
    :return:
    """

    if type(card_or_account_number) is str:

        if len(str(card_or_account_number)) > 0:
            n_f_m = ""
            name_mask = ""
            for i in str(card_or_account_number):
                if i.isdigit() is True:
                    n_f_m += i
                else:
                    name_mask += i

            if n_f_m != "" and name_mask != "":

                if len(n_f_m) == 20 and re.findall(r"\b[Сс]ч[е|ё]т\b\s", name_mask) is not None:
                    result = f"**{n_f_m[16:]}"
                    total_result = name_mask + result
                    return total_result

                elif 13 <= len(n_f_m) <= 19 and len(n_f_m) != 14 and len(n_f_m) != 17 and n_f_m.isdigit() is True:
                    number = str(n_f_m)
                    star = "*"
                    result = f"{number[:4]} {number[4:6]}** {star * (len(number) - 12)} {number[-4:]}"
                    total_result = name_mask + result
                    return total_result

                return "некорректный ввод данных"

            return "некорректный ввод данных"

        return "пустой ввод"
    else:
        raise TypeError("получен аргумент некорректного типа")

    # except TypeError as e:
    #   return f"TypeError: {e}"


def get_date(formatted_date: Any | str) -> str | None:
    """
    Функция преобразует полученную строку с датой в дату формата 'ДД.ММ.ГГГГ'
    :param formatted_date:
    :return:
    """
    if formatted_date is not None:
        received_date = re.search(r".*(\d{4}).(\d{2}).(\d{2}).*", formatted_date)

        if received_date is not None:
            result = f"{received_date.group(3)}.{received_date.group(2)}.{received_date.group(1)}"
            return result
        else:
            return "пустой ввод"





# trans = get_read_file('../data/operations.json')
# for dict in trans:
#     date = dict["date"]
#     print(get_date(date))
# date = ""
# print(get_date(date))
