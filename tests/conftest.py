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


@pytest.fixture
def list_dicts_with_transactions() -> [list[dict[str, Any]]]:
    """Возвращает список словарей для теста с неверным форматом даты"""
    return [
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


@pytest.fixture
def list_dict_zero_for_test() -> list:
    """Возвращает список словарей для теста с неверным форматом даты"""
    return []


@pytest.fixture
def list_dict_incomplete_data_for_test() -> list[dict[str, Any]]:
    """Возвращает список словарей для теста с неверным форматом даты"""
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        },
    ]


@pytest.fixture
def currency_filter_1() -> str:
    """Возвращает тип валюты 'USD'"""
    return "USD"


@pytest.fixture
def currency_filter_2() -> str:
    """Возвращает тип валюты 'EUR'"""
    return "EUR"


@pytest.fixture
def list_dict_after_filter_by_currency() -> list[dict[str, Any]]:
    """Возвращает список словарей для теста с неверным форматом даты"""
    return [
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
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def apilayer_return() -> dict:
    """Возвращает словарь с данными о конвертации транзакции
    (ответ сайта `https://api.apilayer.com`)"""
    return {
        "date": "2025-01-15",
        "info": {"rate": 103.003538, "timestamp": 1736854983},
        "query": {"amount": 50, "from": "EUR", "to": "RUB"},
        "result": 5287.71715,
        "success": True,
    }


@pytest.fixture
def data_eur() -> list[dict]:
    """Возвращает словарь с транзакцией"""
    return [
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "50.0", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        }
    ]


@pytest.fixture
def data_rub_no_currency() -> list[dict]:
    """Возвращает словарь с транзакцией"""
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": ""}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@pytest.fixture
def data_for_test_1() -> str:
    return """[
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]"""


@pytest.fixture
def data_for_test_invalid() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
