from unittest.mock import patch
from unittest.mock import mock_open, patch

import pytest

from decorators import log
from src.utils import get_read_file


def test_get_read_file_success(data_for_test_utils):
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""
    mocked_open = mock_open(read_data=data_for_test_utils)
    with patch('builtins.open', mocked_open):
        result = get_read_file('builtins.open')
        assert result == '''[
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
]'''


def test_get_read_file_invalid(data_for_test_utils_invalid):
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""
    mocked_open = mock_open(read_data=data_for_test_utils_invalid)
    with patch('builtins.open', mocked_open):
        result = get_read_file('builtins.open')
        assert result == []


def test_get_read_file_decode_error_console(data_for_test_utils_invalid, capsys):
    """Проверяет вывод в консоль ошибки `JSONDecodeError`, если невозможно
    декодировать (преобразовать) JSON-данные, содержащиеся в файле"""
    mocked_open = mock_open(read_data=data_for_test_utils_invalid)
    with patch('builtins.open', mocked_open):
        print(get_read_file('builtins.open'))
        captured = capsys.readouterr()
        assert captured.out == 'JSONDecodeError: Invalid JSON data.\n[]\n'


def test_get_read_file_decode_error_return(data_for_test_utils_invalid):
    """Проверяет, что функция возвращает пустой список, если возникает ошибка
    `JSONDecodeError`, когда невозможно декодировать (преобразовать) JSON-данные,
    содержащиеся в файле"""
    mocked_open = mock_open(read_data=data_for_test_utils_invalid)
    with patch('builtins.open', mocked_open):
        result = get_read_file('builtins.open')
        assert result == []


def test_get_read_file_not_found_console(capsys):
    """Проверяет, что при отсутствии файла для чтения данных выдается
    соответствующее сообщение в консоль"""
    print(get_read_file('test.json'))
    captured = capsys.readouterr()
    assert captured.out == 'FileNotFoundError: Файл не найден.\n[]\n'


def test_get_read_file_not_found_return():
    """Проверяет, что при отсутствии файла для чтения данных функция
    возвращает пустой список"""
    result = get_read_file('test.json')
    assert result == []



    # def mock_get_exchange_rate(currency):
    #     return 75.0  # например, фиксированный курс для теста
    #
    # with patch('external_api.get_exchange_rate', new=mock_get_exchange_rate):
# здесь ты можешь вызывать код, который использует get_exchange_rate
# и он будет использовать mock_get_exchange_rate вместо оригинальной функции