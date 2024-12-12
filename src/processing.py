def filter_by_state(list_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и параметр state, по которому фильтрует список"""
    new_list_dictionaries = []
    for dictionary in list_dictionaries:
        for value in dictionary.values():
            if value == state:
                new_list_dictionaries.append(dictionary)

    return new_list_dictionaries