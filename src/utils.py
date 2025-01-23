import json
import logging
from json import JSONDecodeError
from typing import Any

utils_logger = logging.getLogger("get_read_file")
file_handler = logging.FileHandler("./logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_read_file(path_to_file: str) -> str | list[dict] | Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях, логирует результаты выполнения функции в файл
    :param path_to_file:
    :return:
    """
    utils_logger.info(f'\nПолучен путь к JSON-файлу для чтения - "{path_to_file}"')
    try:
        with open(path_to_file, encoding="utf-8") as file:
            try:
                operations_data = json.load(file)
                utils_logger.info(
                    f"\nДанные из JSON-формата успешно преобразованы в список словарей "
                    f"\nс данными о финансовых транзакциях и выведены в консоль в следующем виде:"
                    f"\n{operations_data}"
                )

            except JSONDecodeError as exc_info:
                print("JSONDecodeError: Invalid JSON data.")
                utils_logger.error(
                    f"\nFunction '{get_read_file.__name__}' error: {type(exc_info).__name__}: {str(exc_info)}."
                )
                return []

    except FileNotFoundError as exc_info:
        print("FileNotFoundError: Файл не найден.")
        utils_logger.error(f"\nFunction '{get_read_file.__name__}' error: {type(exc_info).__name__}.")
        return []

    return operations_data


def main_read_1() -> str | list[dict] | Any:
    """Логирует тесты функции `get_read_file()`"""
    utils_logger.info("\nЗапуск приложения c тестовыми данными")
    utils_logger.info("\nТест_№1")
    result_1 = get_read_file("./data/operations.json")
    utils_logger.info("\nЗавершение работы приложения\n")
    return result_1


def main_read_2() -> str | list[dict] | Any:
    """Логирует тесты функции `get_read_file()`"""
    utils_logger.info("\nЗапуск приложения c тестовыми данными")
    utils_logger.info("\nТест_№2")
    result_2 = get_read_file("../data/operations.json")
    utils_logger.info("\nЗавершение работы приложения\n\n")
    return result_2


def main_read_3() -> str | list[dict] | Any:
    """Логирует тесты функции `get_read_file()`"""
    utils_logger.info("\nЗапуск приложения c тестовыми данными")
    utils_logger.info("\nТест_№3")
    result_3 = get_read_file("./data/operations_error.json")
    utils_logger.info("\nЗавершение работы приложения\n\n")
    return result_3


# print(get_read_file('../data/operations.json'))
