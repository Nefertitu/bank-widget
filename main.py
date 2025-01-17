import os
from typing import Any

from decorators import my_function
from src.external_api import data_for_test_rub, get_conversion_apilayer, get_random_number
from src.generators import card_number_generator, filter_by_currency, transactions_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import get_read_file
from src.widget import get_data, mask_account_card

if __name__ == "__main__":

    print(mask_account_card("Visa Platinum 7000792289606361"))
    print()

    print(mask_account_card("Счет 64686473678894779589"))
    print()

    print(get_data("2024-03-11T02:26:18.671407"))
    print()

    transaction_list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    print(filter_by_state(transaction_list, state="CANCELED"))
    print()

    transaction_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    print(sort_by_date(transaction_list, sort_order=False))
    print()

    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    result_filter = filter_by_currency(transactions, "EUR")

    while True:
        try:
            print(next(result_filter))

        except StopIteration:
            print("генератор исчерпан")
            print()
            break

    descriptions = transactions_descriptions(transactions)

    for count in range(5):
        print(next(descriptions))
        count += 1

    print()

    for card_number in card_number_generator(5, 1):
        print(card_number)
        print()

    print(my_function(1, 5))
    print(my_function(1, "5"))
    print(my_function(1, 0))
    print()


def path() -> str:
    """
    Возвращает путь к файлу `operations.json`
    :return:
    """

    path_to_file = os.path.join(os.getcwd(), "data", "operations.json")

    return path_to_file


def main() -> int | str | list[dict[Any, Any]] | Any:
    """
    Объединяет действия других функций:
    - чтение JSON-файла с транзакциями;
    - рандомный выбор словаря с данными о транзакциях;
    - возврат суммы транзакции из выбранного словаря в рублях;
    - обращение к внешнему API для получения текущего курса валют и конвертации суммы операции
    в рубли, если транзакция была выполнена в другой валюте
    :return:
    """
    path_to_file = path()
    data_transactions = get_read_file(path_to_file)
    random_number = get_random_number(data_transactions)
    result_transactions = get_conversion_apilayer(random_number, data_transactions)

    return result_transactions


def main_rub() -> str | list[dict[Any, Any]] | Any:
    """
    Объединяет действия других функций:
    - получение данных из файла с транзакциями, проведенными в рублях;
    - рандомный выбор словаря с данными о транзакциях;
    - возврат суммы транзакции из выбранного словаря
    :return:
    """

    transactions_rub = data_for_test_rub()
    random_number = get_random_number(transactions_rub)
    result_transactions = get_conversion_apilayer(random_number, transactions_rub)

    return result_transactions


if __name__ == "__main__":

    print(main())
    print()

    print(main_rub())
