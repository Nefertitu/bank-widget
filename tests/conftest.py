from typing import Any

import pytest


@pytest.fixture
def card_number_for_test() -> str:
    """Возвращает маску номера карты"""
    return "7000 79** **** 6361"


@pytest.fixture
def account_number_for_test() -> str:
    """Возвращает номер счета"""
    return "73654108430135874305"


@pytest.fixture
def account_card_error_number_for_test() -> int:
    """Возвращает номер счета типа `int`"""
    return 73654108430133051111


@pytest.fixture
def data_for_test() -> str:
    """Возвращает строку с датой"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def list_dict_for_test() -> list[dict[str, Any]]:
    """Возвращает список словарей для теста"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def state_for_test() -> str:
    """Возвращает значение `state`"""
    return "CANCELED"


@pytest.fixture
def list_dict_for_test_incorrect_format() -> list[dict[str, Any]]:
    """Возвращает список словарей для теста с неверным форматом даты"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/10/14T0"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def order_for_test() -> bool:
    """Возвращает значение `order`"""
    return True
