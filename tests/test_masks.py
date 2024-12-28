from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_for_test: str) -> None:
    """
    Функция тестирует правильность маскирования номера карты стандартной длины
    (16 символов)
    :param card_number_for_test:
    :return:
    """

    assert get_mask_card_number("7000792289606361") == card_number_for_test


def test_get_mask_card_number_zero() -> None:
    """
    Функция тестирует корректность обработки пустого ввода номера карты
    :return:
    """

    assert get_mask_card_number("") == "пустой ввод"


# декоратор для запуска тестирования с различными входными данными
# (нестандартная длина номера карт)
@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792286361", "7000 79** * 6361"),
        ("700079228996361", "7000 79** *** 6361"),
        ("700079228960126361", "7000 79** ****** 6361"),
        ("7000792289601236361", "7000 79** ******* 6361"),
    ],
)
def test_get_mask_card_number_other_length(value: str, expected: list[dict[str, Any]]) -> None:
    """
    Проверка работы функции (`get_mask_card_number`) для номеров карт
    различной длины с использованием параметризации
    :param value:
    :param expected:
    :return:
    """

    assert get_mask_card_number(value) == expected


def test_get_mask_account(account_number_for_test: str) -> None:
    """
    Функция тестирует правильность маскирования номера счета
    :param account_number_for_test:
    :return:
    """

    assert get_mask_account(account_number_for_test) == "**4305"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305111", "некорректный ввод данных"),
        ("73654108430", "некорректный ввод данных"),
        ("!№;%:?*()_+)(*?:%;№!", "некорректный ввод данных"),
        ("ВАПРОолд__еутЗД79432", "некорректный ввод данных"),
    ],
)
def test_get_mask_account_incorrect_input(value: str, expected: list[dict[str, Any]]) -> None:
    """
    Проверка работы функции (`get_mask_account`) при некорректном вводе данных
    (длина номера счета больше или меньше 20 символов, введенные данные
    не являются цифрами)
    :param value:
    :param expected:
    :return:
    """

    assert get_mask_account(value) == expected


def test_get_mask_account_zero() -> None:
    """
    Функция тестирует корректность обработки пустого ввода номера счета
    :return:
    """

    assert get_mask_account("") == "пустой ввод"
