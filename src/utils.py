import json
import os

from json import JSONDecodeError
from typing import Any


def get_read_file(path: str) -> str | list[dict] | Any:
    try:
        with open(path, encoding='utf-8') as file:
            try:
                operations_data = json.load(file)
                operations_json = json.dumps(operations_data, indent=2, ensure_ascii=False)

            except JSONDecodeError:
                print('JSONDecodeError: Invalid JSON data.')
                return []

    except FileNotFoundError:
        print('FileNotFoundError: Файл не найден.')
        return []

    return operations_json


def path():
    """

    :return:
    """
    path_to_file = os.path.join(os.path.dirname(os.getcwd()), 'data','operations.json')

    return path_to_file


path_to_file = path()

print(get_read_file(path_to_file))

