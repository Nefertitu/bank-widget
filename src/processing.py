def filter_by_state(list_dictionaries: list[dict[str, str]], state: str = "EXECUTED") -> list[dict[str, str]]:
    """Фильтрует список словарей с данными о банковских операциях по параметру state"""
    new_list_dictionaries = []
    for dictionary in list_dictionaries:
        for value in dictionary.values():
            if value == state:
                new_list_dictionaries.append(dictionary)

    return new_list_dictionaries


def sort_by_date(list_dictionaries: list[dict[str, str]], sort_order: bool = True) -> list[dict[str, str]]:
    """Сортирует полученный список словарей по дате, параметр, задающий порядок сортировки, по умолчанию - убывание"""
    if sort_order is True:
        sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary["date"], reverse=True)
    else:
        sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary["date"])

    return sorted_dictionaries
