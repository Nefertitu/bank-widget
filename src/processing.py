def filter_by_state(list_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Функция принимает список словарей с данными о банковских операциях и параметр state, по которому фильтрует список"""
    new_list_dictionaries = []
    for dictionary in list_dictionaries:
        for value in dictionary.values():
            if value == state:
                new_list_dictionaries.append(dictionary)

    return new_list_dictionaries


# list = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(list, state="CANCELED"))
