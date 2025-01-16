import random
from unittest import mock
from wsgiref import headers

from requests.exceptions import Timeout
from typing import Callable
from unittest.mock import patch, MagicMock, Mock

import pytest
import requests.exceptions

from src.external_api import get_conversion_apilayer, get_random_number, transactions_test, apilayer_key
from tests.conftest import apilayer_return, data_eur


def test_get_random_number():
    """Проверяет, что функция вернет заданное в объекте Mock() число
    и объект Mock будет вызван с данным аргументом один раз"""
    mock_random = Mock(return_value=3)
    random.randint = mock_random
    assert get_random_number(transactions_test) == 3
    mock_random.assert_called_once_with(0, len(transactions_test) - 1)


def test_get_random_number_one_transaction(data_eur):
    """Проверяет, что функция вернет '1', если количество транзакций равно '1'
    и объект Mock не будет вызван с данным аргументом"""
    mock_random = Mock(return_value=1)
    random.randint = mock_random
    assert get_random_number(data_eur) == 1
    mock_random.assert_not_called()


@patch('requests.get')
def test_get_conversion_apilayer_success(mock_requests, data_eur, apilayer_return):
    """
    Проверяет, что функция возвращает ожидаемое значение, и что функция
    `requests.get` была вызвана только один раз с правильным URL
    :param mock_requests:
    :param data_eur:
    :param apilayer_return:
    :return:
    """
    mock_requests.return_value.json.return_value = apilayer_return
    assert get_conversion_apilayer(0, data_eur) == f'Сумма транзакции составляет 50 EUR или {round(mock_requests.return_value.json.return_value['result'], 2)} рублей в соответствии с текущим курсом валют на дату: {mock_requests.return_value.json.return_value['date']}.'
    mock_requests.assert_called_once_with(f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=50.0', headers={'apikey': apilayer_key}, data={}, timeout=10)


@patch('requests.get')
def test_get_conversion_apilayer_raises_timeout(mock_requests, data_eur):
    mock_requests.exceptions = requests.exceptions
    # mock_response = MagicMock(status_code=408, match="Request timed out. Please check your internet connection.")
    mock_requests.get.side_effect = Timeout("Request timed out. Please check your internet connection.")
    mock_requests.get_return_value = "Request timed out. Please check your internet connection."

    assert requests.get() == "Request timed out. Please check your internet connection."


@patch('requests.get')
def test_get_conversion_apilayer_exception(mock_requests, data_eur):
    exception = requests.RequestException(mock.Mock(status_code=404), 'not found')
    mock_requests(mock.ANY).raise_for_status_effect = exception

    with pytest.raises(requests.RequestException) as error_info:
        get_conversion_apilayer(0, data_eur)
        assert error_info == exception

@patch('requests.get')
def test_get_conversion_apilayer_raises_http_error(mocked_get, data_eur):
    mocked_get = Mock(status_code=403)
    requests.get = mocked_get
    mocked_get.return_value.json.return_value = {'message': 'HTTP Error. Please check the URL.'}
    assert requests.get() == 'HTTP Error. Please check the URL.'

    # res = get_conversion_apilayer(0, data_eur)
    # assert res == 'HTTP Error. Please check the URL.'
    # with patch('requests.get', return_value=mock_response):
    # with pytest.raises(requests.exceptions.HTTPError) as err_msg:
    #     res.raise_for_status()
    # print(err_msg)

    # mock_requests.get.side_effect = requests.exceptions.HTTPError("HTTP Error. Please check the URL.")
    # mock_requests.get_return_value = mock_response
    # assert get_conversion_apilayer('USD', 10) ==  "HTTP Error. Please check the URL."


def test_get_conversion_apilayer_no_connection(mock_connection):
    mock_connection.return_value = "Connection Error. Проверьте сетевое подключение"
    # with pytest.raises(ConnectionError, match="Connection Error. Проверьте сетевое подключение"):
    assert get_conversion_apilayer("USD", 10) == f'{mock_connection.return_value}'


def test_get_conversion_apilayer_except( data_eur):
    with pytest.raises(ExceptionGroup):
        get_conversion_apilayer(0, data_eur)