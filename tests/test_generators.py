from typing import Any

import pytest

from src.generators import transactions_descriptions, card_number_generator, filter_by_currency


def test_filter_by_currency_(list_dicts_with_transactions: list[dict[str, Any]], currency_filter_1: str) -> None:
    """Тест, проверяющий, что функция `filter_by_currency` корректно фильтрует
    транзакции по заданной валюте"""

    generator = filter_by_currency(list_dicts_with_transactions, currency_filter_1)
    expected_result1 = {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
    expected_result2 = {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
    expected_result3 = {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}

    assert next(generator) == expected_result1
    assert next(generator) == expected_result2
    assert next(generator) == expected_result3


def test_filter_by_missing_currency(list_dicts_with_transactions: list[dict[str, Any]], currency_filter_2: str) -> None:
    """Тест, проверяющий, что функция `filter_by_currency` правильно обрабатывает случаи,
    когда транзакции в заданной валюте отсутствуют"""

    generator = filter_by_currency(list_dicts_with_transactions, currency_filter_2)
    expected_result = f"нет операций в валюте '{currency_filter_2}'"

    assert next(generator) == expected_result



def test_filter_by_currency_zero_list(list_dict_zero_for_test: list, currency_filter_1: str) -> None:
    """Тест, проверяющий, что функция `filter_by_currency` корректно фильтрует
    транзакции по заданной валюте"""

    generator = filter_by_currency(list_dict_zero_for_test, currency_filter_1)
    expected_result = "пустой список"

    assert next(generator) == expected_result


# def test_transaction_descriptions(list_dicts_with_transactions: list[dict[str, Any]]) -> None:
#     """Тест, проверяющий, что функция `transaction_descriptions` возвращает корректные
#         описания для каждой транзакции"""
#
#     generator = transactions_descriptions(list_dicts_with_transactions)
#     expected_result1 = "Перевод организации"
#     expected_result2 = "Перевод со счета на счет"
#     expected_result3 = "Перевод со счета на счет"
#     expected_result4 = "Перевод с карты на карту"
#     expected_result5 = "Перевод организации"
#
#     assert next(generator) == expected_result1
#     assert next(generator) == expected_result2
#     assert next(generator) == expected_result3
#     assert next(generator) == expected_result4
#     assert next(generator) == expected_result5
#
#
# def test_card_number_generator():
#     assert card_number_generator()
#     pass