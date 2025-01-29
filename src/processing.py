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
            else:
                continue
    if new_list_dictionaries:
        return new_list_dictionaries
    return "нет данных"


def sort_by_date(list_dictionaries: list[dict[str, Any]], sort_order: bool = True) -> Any:
    """
    Сортирует полученный список словарей по дате, порядок сортировки, -
    по умолчанию - убывание
    :param list_dictionaries:
    :param sort_order:
    :return:
    """

    comparsion_dictionaries = []
    for dictionary in list_dictionaries:
        if dictionary != {}:
            pattern = r"\d{4}[-]\d{2}[-]\d{2}.*"
            match = re.search(pattern, dictionary["date"])
            if match:
                comparsion_dictionaries.append(dictionary)
            if match is None:
                continue
        if dictionary == {}:
            continue
    if len(comparsion_dictionaries) != len(list_dictionaries):
        return "неверный формат даты"
    else:
        if sort_order is True:
            sorted_dictionaries = sorted(comparsion_dictionaries, key=lambda dictionary: dictionary["date"],
                                         reverse=True)
        else:
            sorted_dictionaries = sorted(comparsion_dictionaries, key=lambda dictionary: dictionary["date"])

        return sorted_dictionaries



# list_dict = get_read_file('../data/operations.json')
# list_dict = get_read_excel('../transactions_excel.xlsx')
# list_dict = get_read_csv('../transactions.csv')
list_dict = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/10/14T0"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
# print(list_dict)
# list_dict = transactions_sort_status
print(sort_by_date(list_dict, sort_order=False))

# print(sort_by_date(list_dict, sort_order=True))
