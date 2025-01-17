import json
from json import JSONDecodeError
from typing import Any


def get_read_file(path_to_file: str) -> str | list[dict] | Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    :param path_to_file:
    :return:
    """
    try:
        with open(path_to_file, encoding="utf-8") as file:
            try:
                operations_data = json.load(file)

            except JSONDecodeError:
                print("JSONDecodeError: Invalid JSON data.")
                return []

    except FileNotFoundError:
        print("FileNotFoundError: Файл не найден.")
        return []

    return operations_data


# print(get_read_file('../data/operations.json'))
