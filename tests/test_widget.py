from typing import Any

import pytest

from src.widget import get_data, mask_account_card


# декоратор для запуска тестирования с различными входными данными
# (номера счетов, номера карт)
@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Card 7158300734726758", "Card 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("МИР 7000792289601236361", "МИР 7000 79** ******* 6361"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    """
    Проверяет, что функция корректно распознает и применяет нужный тип маскировки
    в зависимости от типа входных данных (карта или счет)
    :param value:
    :param expected:
    :return:
    """

    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305111", "некорректный ввод данных"),
        ("Карта 73654108430", "некорректный ввод данных"),
        ("Счет !№;%:?*()_+)(*?:%;№!", "некорректный ввод данных"),
        ("Visa Platinum 123456олд__еутЗД794", "некорректный ввод данных"),
    ],
)
def test_mask_account_card_incorrect_input(value: str, expected: list[dict[str, Any]]) -> None:
    """
    Проверка работы функции (`get_mask_account`) при некорректном вводе данных (длина
    номера счета больше или меньше 20 символов, введенные данные не являются цифрами)
    :param value:
    :param expected:
    :return:
    """

    assert mask_account_card(value) == expected


def test_mask_account_card_zero() -> None:
    """
    Функция тестирует корректность обработки пустого ввода номера карты или счета
    :return:
    """

    assert mask_account_card("") == "пустой ввод"


def test_mask_account_card_error(account_card_error_number_for_test: str) -> None:
    """
    Функция проверяет, что некорректный ввод данных номера карты (например, введены
    данные типа int вместо str) приводит к возникновению исключения 'TypeError'
    :param account_card_error_number_for_test:
    :return:
    """

    with pytest.raises(TypeError) as exc_info:
        mask_account_card(account_card_error_number_for_test)

        assert str(exc_info.value) == "TypeError: получен аргумент некорректного типа"
        print(exc_info)


def test_get_data(data_for_test: str) -> None:
    """
    Тестирование правильности преобразования даты
    :param data_for_test:
    :return:
    """

    assert get_data(data_for_test) == "11.03.2024"


def test_get_data_zero() -> None:
    """
    Тестирование работы функции на корректность обработки пустого ввода
    :param:
    :return:
    """

    assert get_data("") == "пустой ввод"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("T02:26:18.6714072024-03-11", "11.03.2024"),
        ("T02:26:18.6714072024.03.11", "11.03.2024"),
        ("2024/03/11T02:26:18.671407", "11.03.2024"),
        ("2024|03|11", "11.03.2024"),
    ],
)
def test_get_data_incorrect_input(value: str, expected: list[dict[str, Any]]) -> None:
    assert get_data(value) == expected
