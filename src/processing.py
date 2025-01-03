import re
from typing import Any


def filter_by_state(list_dictionaries: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """
    Фильтрует список словарей с данными о банковских операциях по параметру 'state'
    :param list_dictionaries:
    :param state:
    :return:
    """

    new_list_dictionaries = []
    for dictionary in list_dictionaries:
        for value in dictionary.values():
            if value == state:
                new_list_dictionaries.append(dictionary)
    if new_list_dictionaries:
        return new_list_dictionaries
    return "нет данных"


def sort_by_date(list_dictionaries: list[dict[str, Any]], sort_order: bool = True) -> Any:
    """
    Сортирует полученный список словарей по дате, параметр, задающий порядок сортировки,
    по умолчанию - убывание
    :param list_dictionaries:
    :param sort_order:
    :return:
    """

    comparsion_dictionary = []
    for dictionary in list_dictionaries:
        if re.search(r"\d{4}-\d{2}-\d{2}.*", dictionary["date"]):
            comparsion_dictionary.append(dictionary)
        else:
            continue
    if comparsion_dictionary != list_dictionaries:
        return "неверный формат даты"

    else:
        if sort_order is True:
            sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary["date"], reverse=True)
        else:
            sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary["date"])

        return sorted_dictionaries
