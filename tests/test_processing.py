from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_dict_for_test: list[dict[str, Any]], state_for_test: str) -> None:
    """
    Тестирование функции фильтрации списка словарей по заданному статусу 'state'
    :param list_dict_for_test:
    :param state_for_test:
    :return:
    """

    assert filter_by_state(list_dict_for_test, state_for_test) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "value, state, expected",
    [
        (
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            "EXECUTED",
            "нет данных",
        ),
        (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            "CANCELED",
            "нет данных",
        ),
    ],
)
def test_filter_by_state_none(value: list[dict[str, Any]], state: str, expected: str) -> None:
    """
    Тестирование функции фильтрации списка словарей при отсутствии словарей с указанным
    статусом 'state'
    :param value:
    :param state:
    :param expected:
    :return:
    """

    assert filter_by_state(value, state) == "нет данных"


@pytest.mark.parametrize(
    "value, order, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(value: list[dict[str, Any]], order: bool, expected: list[dict[str, Any]]) -> None:
    """
    Тестирование сортировки списка словарей по датам в порядке убывания или возрастания
    (в зависимости то указанного параметра `order` - True или False)
    :param value:
    :param order:
    :param expected:
    :return:
    """

    assert sort_by_date(value, order) == expected


@pytest.mark.parametrize(
    "value, order, expected",
    [
        (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30"},
            ],
        ),
        (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_same_dates(value: list[dict[str, Any]], order: bool, expected: list[dict[str, Any]]) -> None:
    """
    Тестирование сортировки списка словарей в порядке убывания или возрастания
    (в зависимости то указанного параметра `order` - True или False) при одинаковых датах
    :param value:
    :param order:
    :param expected:
    :return:
    """

    assert sort_by_date(value, order) == expected


def test_sort_by_date_incorrect_format(
    list_dict_for_test_incorrect_format: list[dict[str, Any]], order_for_test: bool
) -> None:
    """
    Тестирует работу функции с некорректными или нестандартными форматами дат
    :param list_dict_for_test_incorrect_format:
    :param order_for_test:
    :return:
    """

    assert sort_by_date(list_dict_for_test_incorrect_format, order_for_test) == "неверный формат даты"
