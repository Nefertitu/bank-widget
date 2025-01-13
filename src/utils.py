import json
import os

from json import JSONDecodeError

path_to_dir = str(os.path.dirname(__file__).replace('src', 'data'))
file_name = 'operations.json'
path_to_file = os.path.join(path_to_dir, file_name)


def get_read_file(path: str) -> list[dict]:
    try:
        with open(path, encoding='utf-8') as file:
            try:
                operations_data = json.load(file)
            except JSONDecodeError:
                print('Ошибка декодирования файла')
                return []
    except FileNotFoundError:
        print('Файл не найден')
        return []

    return operations_data


print(get_read_file(path_to_file))