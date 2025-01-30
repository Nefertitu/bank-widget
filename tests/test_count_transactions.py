from collections import Counter
from typing import Any

import pytest

from src.count_transactions import get_count_transactions


@pytest.mark.parametrize(
    "value, categories, expected",
    [
        (
            [
                {"amount": "79931.03", "currency": "RUB", "description": "Открытие вклада"},
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
            ],
            ["открытие вклада", "перевод организации"],
            Counter({"Открытие вклада": 1, "Перевод организации": 1}),
        ),
        (
            [
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
                {"amount": "8221.37", "code": "USD", "description": "Перевод со счета на счет"},
            ],
            ["перевод организации", "перевод со счета на счет"],
            Counter({"Перевод организации": 1, "Перевод со счета на счет": 1}),
        ),
        ([], ["Открытие вклада"], Counter()),
    ],
)
def test_get_count_transactions(value: list[dict], categories: list, expected: Counter[Any] | str) -> None:
    """
    Тестирование функции подсчета количества банковских операций по заданным категориям
    :param value:
    :param string_search:
    :return:
    """
    assert get_count_transactions(value, categories) == expected
