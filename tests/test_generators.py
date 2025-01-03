from typing import Any, Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transactions_descriptions


def test_filter_by_currency_(list_dicts_with_transactions: list[dict[str, Any]], currency_filter_1: str) -> None:
    """
    Тест, проверяющий, что функция `filter_by_currency` корректно фильтрует
    транзакции по заданной валюте
    :param list_dicts_with_transactions:
    :param currency_filter_1:
    :return:
    """

    generator = filter_by_currency(list_dicts_with_transactions, currency_filter_1)
    expected_result1 = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    expected_result2 = {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    expected_result3 = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    assert next(generator) == expected_result1
    assert next(generator) == expected_result2
    assert next(generator) == expected_result3


def test_filter_by_missing_currency(
    list_dicts_with_transactions: list[dict[str, Any]], currency_filter_2: str
) -> None:
    """
    Тест, проверяющий, что функция `filter_by_currency` правильно обрабатывает случаи,
    когда транзакции в заданной валюте отсутствуют
    :param list_dicts_with_transactions:
    :param currency_filter_2:
    :return:
    """

    generator = filter_by_currency(list_dicts_with_transactions, currency_filter_2)
    expected_result = f"нет операций в валюте '{currency_filter_2}'"

    assert next(generator) == expected_result


def test_filter_by_currency_zero_list(list_dict_zero_for_test: list, currency_filter_1: str) -> None:
    """
    Тест, проверяющий, что функция `filter_by_currency` корректно фильтрует
    транзакции по заданной валюте
    :param list_dict_zero_for_test:
    :param currency_filter_1:
    :return:
    """

    generator = filter_by_currency(list_dict_zero_for_test, currency_filter_1)
    expected_result = "пустой список"

    assert next(generator) == expected_result


def test_transaction_descriptions(list_dicts_with_transactions: list[dict[str, Any]]) -> None:
    """
    Тест, проверяющий, что функция `transaction_descriptions` возвращает корректные
    описания для каждой транзакции
    :param list_dicts_with_transactions:
    :return:
    """

    generator = transactions_descriptions(list_dicts_with_transactions)
    expected_result1 = "Перевод организации"
    expected_result2 = "Перевод со счета на счет"
    expected_result3 = "Перевод со счета на счет"
    expected_result4 = "Перевод с карты на карту"
    expected_result5 = "Перевод организации"

    assert next(generator) == expected_result1
    assert next(generator) == expected_result2
    assert next(generator) == expected_result3
    assert next(generator) == expected_result4
    assert next(generator) == expected_result5


def test_transaction_descriptions_zero(list_dict_zero_for_test: list) -> None:
    """
    Тест, проверяющий, что функция `transaction_descriptions` возвращает корректные
    описания для каждой транзакции
    :param list_dict_zero_for_test:
    :return:
    """

    generator = transactions_descriptions(list_dict_zero_for_test)
    expected_result = "пустой список"

    assert next(generator) == expected_result


def test_transaction_descriptions_incomplete_data(list_dict_incomplete_data_for_test: list) -> None:
    """
    Тест, проверяющий, что функция `transaction_descriptions` корректно обрабатывает
    пустой список
    :param list_dict_incomplete_data_for_test:
    :return:
    """

    generator = transactions_descriptions(list_dict_incomplete_data_for_test)
    expected_result = "отсутствуют данные о проведенных операциях"

    assert next(generator) == expected_result


@pytest.mark.parametrize(
    "start_number, stop_number, expected_value",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (115, 117, ["0000 0000 0000 0115", "0000 0000 0000 0116", "0000 0000 0000 0117"]),
        (11111, 11114, ["0000 0000 0001 1111", "0000 0000 0001 1112", "0000 0000 0001 1113", "0000 0000 0001 1114"]),
    ],
)
def test_card_number_generator(start_number: int, stop_number: int, expected_value: Iterator[list[str]]) -> None:
    """
    Тест, проверяющий, что генератор 'card_number_generator' выдает правильные
    номера карт в заданном диапазоне
    :param start_number:
    :param stop_number:
    :param expected_value:
    :return:
    """

    generator = card_number_generator(start_number, stop_number)
    # for item in (generator):
    assert list(generator) == expected_value


@pytest.mark.parametrize(
    "start_number, stop_number, expected_value",
    [
        (0, 0, ["номер карты не может быть равным '0' и не должен превышать '9999 9999 9999 9999'"]),
        (
            10000000000000000,
            10000000000000000,
            ["номер карты не может быть равным '0' и не должен превышать '9999 9999 9999 9999'"],
        ),
        (
            9999999999999999,
            9999999999999999,
            ["!!!доcтигнуто предельное значение номера карты - '9999 9999 9999 9999'!!!"],
        ),
    ],
)
def test_card_number_generator_limit_values(
    start_number: int, stop_number: int, expected_value: Iterator[list[str]]
) -> None:
    """
    Тест, проверяющий, что генератор 'card_number_generator' правильно обрабатывает крайние
    значения диапазона и правильно завершает генерацию
    :param start_number:
    :param stop_number:
    :param expected_value:
    :return:
    """

    generator = card_number_generator(start_number, stop_number)

    assert list(generator) == expected_value


def test_card_number_generator_incorrect_input() -> None:
    """
    Тест, проверяющий, что генератор 'card_number_generator' правильно обрабатывает
    некорректный ввод данных
    :return:
    """

    generator = card_number_generator(1, "55")

    assert list(generator) == ["Ошибка: некорректный ввод"]


def test_card_number_generator_start_more() -> None:
    """
    Тест, проверяющий, что замена местами значений 'stop' И 'start' ('start' > 'stop')
    не влияет на результат теста(номера карт генерируются от меньшего к большему)
    :return:
    """

    generator = card_number_generator(5, 1)
    expected_result = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    assert list(generator) == expected_result
