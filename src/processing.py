import pandas as pd
import re
from typing import Any

from src.read_transactions import get_read_excel, get_read_csv
from src.utils import get_read_file


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
            else:
                continue
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

    comparsion_dictionaries = []
    for dictionary in list_dictionaries:
        if dictionary != {}:
            pattern = r"\d{4}-\d{2}-\d{2}.*"
            match = re.search(pattern, dictionary["date"])
            if match:
                comparsion_dictionaries.append(dictionary)
            if match is None:
                continue
        if dictionary == {}:
            continue
    if sort_order is True:
        sorted_dictionaries = sorted(comparsion_dictionaries, key=lambda dictionary: dictionary["date"], reverse=True)
    else:
        sorted_dictionaries = sorted(comparsion_dictionaries, key=lambda dictionary: dictionary["date"])

    return sorted_dictionaries


# list_dict = get_read_file('../data/operations.json')
# list_dict = get_read_excel('../transactions_excel.xlsx')
# list_dict = get_read_csv('../transactions.csv')
# print(list_dict)
# list_dict = transactions_sort_status
# print(sort_by_date(list_dict, sort_order=False))

# print(sort_by_date(list_dict, sort_order=True))