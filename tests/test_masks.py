from typing import Any

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number_for_test: str):
    """Функция тестирует правильность маскирования номера карты стандартной длины (16 символов)"""
    assert get_mask_card_number("7000792289606361") == card_number_for_test


def test_get_mask_card_number_zero():
    """Функция тестирует корректность обработки пустого ввода номера карты"""
    assert get_mask_card_number("") == "пустой ввод"


def test_get_mask_card_number_error():
    """Функция проверяет, что некорректный ввод данных номера карты (например, два аргумента(два номера карт), вместо одного) приводит к возникновению исключения TypeError"""
    with pytest.raises(TypeError):
        get_mask_card_number("1234567891234678", "123456789123456")


# декоратор для запуска тестирования с различными входными данными (нестандартная длина номера карт)
@pytest.mark.parametrize("value, expected", [
    ("7000792286361", "7000 79** * 6361"),
    ("70007922896361", "7000 79** ** 6361"),
    ("700079228960126361", "7000 79** ****** 6361"),
    ("7000792289601236361", "7000 79** ******* 6361")
])
def test_get_mask_card_number_other_length(value: str, expected: list[dict[str, Any]]):
    """Проверка работы функции (`get_mask_card_number`) для номеров карт различной длины с использованием параметризации"""
    assert get_mask_card_number(value) == expected


def test_get_mask_account(account_number_for_test: str):
    """Функция тестирует правильность маскирования номера счета"""
    assert get_mask_account(account_number_for_test) == "**4305"

@pytest.mark.parametrize("value, expected", [
    ("73654108430135874305111", "введены некорректные данные"),
    ("73654108430", "введены некорректные данные"),
    ("!№;%:?*()_+)(*?:%;№!", "введены некорректные данные"),
    ("ВАПРОолд__еутЗД79432", "введены некорректные данные")
])
def test_get_mask_account_incorrect_input(value: str, expected: list[dict[str, Any]]):
    """Проверка работы функции (`get_mask_account`) при некорректном вводе данных (длина номера счета больше или меньше 20 символов, введенные данные не являются цифрами)"""
    assert get_mask_account(value) == expected


def test_get_mask_account_zero():
    """Функция тестирует корректность обработки пустого ввода номера счета"""
    assert get_mask_account("") == "пустой ввод"


def test_get_mask_account_error():
    """Функция проверяет, что некорректный ввод данных номера счета (например, два аргумента(два номера счета), вместо одного) приводит к возникновению исключения TypeError"""
    with pytest.raises(TypeError):
        get_mask_account("73654108430135874305", "73654108430133051111")