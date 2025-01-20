import random
from unittest.mock import Mock, patch

import pytest
import requests.exceptions
from requests.exceptions import Timeout

from src.external_api import apilayer_key, get_conversion_apilayer, get_random_number


def test_get_random_number():
    """Проверяет, что функция вернет заданное в объекте Mock() число
    и объект Mock будет вызван с данным аргументом один раз"""
    mock_random = Mock(return_value=3)
    random.randint = mock_random
    param = [{}, {}]
    assert get_random_number(param) == 3
    mock_random.assert_called_once_with(0, len(param) - 1)


def test_get_random_number_one_transaction():
    """Проверяет, что функция вернет '1', если количество транзакций равно '1'
    и объект Mock не будет вызван с данным аргументом"""
    mock_random = Mock(return_value=1)
    random.randint = mock_random
    param = [{}]
    assert get_random_number(param) == 1
    mock_random.assert_not_called()


def test_get_random_number_negative():
    """Проверяет, что функция не вызовет ошибку, если будет передан пустой список"""
    param = []
    assert get_random_number(param) == "Список не должен быть пустым"


def test_get_conversion_apilayer_not_key():
    """Проверяет, что будет вызвано исключение KeyError при отсутствии необходимого ключа"""
    param = [{"operationAmount": {"amount": "115248.15", "currency": {"name": "руб."}}}]
    assert get_conversion_apilayer(0, param) == "Error: KeyError, 'code'"


def test_get_conversion_apilayer_not_value():
    """Проверяет, что при отсутствии или некорректном значении ключа 'amount'
    будет вызвано исключение ValueError"""
    param = [{"operationAmount": {"amount": "", "currency": {"name": "руб.", "code": "RUB"}}}]
    assert get_conversion_apilayer(0, param) == "Error: ValueError, could not convert string to float: ''"


def test_get_conversion_apilayer_type_error():
    """Проверяет, что при некорректном значении типа данных принимаемого
    функцией параметра 'data_transactions' будет вызвано исключение TypeError"""
    param = "транзакции, транзакции, транзакции"
    assert get_conversion_apilayer(0, param) == "Error: TypeError, string indices must be integers, not 'str'"


@patch("requests.get")
def test_get_conversion_apilayer_success(mock_requests, data_eur, apilayer_return):
    """
    Проверяет, что функция возвращает ожидаемое значение, и что функция
    `requests.get` была вызвана только один раз с правильным URL
    :param mock_requests:
    :param data_eur:
    :param apilayer_return:
    :return:
    """
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.return_value = apilayer_return
    assert (
        get_conversion_apilayer(0, data_eur) == f"Сумма транзакции составляет 50 EUR или "
        f"{round(mock_requests.return_value.json.return_value['result'], 2)} рублей "
        f"в соответствии с текущим курсом валют на дату: "
        f"{mock_requests.return_value.json.return_value['date']}."
    )
    mock_requests.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=50.0",
        headers={"apikey": apilayer_key},
        data={},
        timeout=5,
    )


@patch("requests.get")
def test_get_conversion_apilayer_raises_timeout(mocked_get, data_eur):
    """
    Проверяет, что при возникновении ошибки `Timeout`, когда запрос не получил
    ответа в течение заданного времени, функция возвращает соответствующее сообщение.
    :param mocked_get:
    :param data_eur:
    :return:
    """
    mocked_get = Mock(status_code=408)
    requests.get = mocked_get
    mocked_get.side_effect = Timeout("Request timed out. Please check your internet connection.")
    assert get_conversion_apilayer(0, data_eur) == "Request timed out. Please check your internet connection."


@patch("requests.get")
def test_get_conversion_apilayer_http_error(mocked_get, data_eur):
    """
    Проверяет, что при возникновении ошибки `HTTPError`, когда полученный ответ
    от сервера не является корректным HTTP-ответом, функция возвращает
    соответствующее сообщение.
    :param mocked_get:
    :param data_eur:
    :return:
    """
    mocked_get = Mock(status_code=403)
    requests.get = mocked_get
    mocked_get.return_value.json.return_value = "HTTP Error. Please check the URL."
    assert get_conversion_apilayer(0, data_eur) == "HTTP Error. Please check the URL."


@patch("requests.get")
def test_get_conversion_apilayer_connection_error(my_mock):
    """Проверяет, что при возникновении ошибки `ConnectionError`, когда запрос не может быть выполнен из-за проблем
    с сетью, функция возвращает соответсвующее сообщение"""
    requests.get.side_effect = requests.exceptions.ConnectionError
    my_mock.side_effect = ConnectionError("ConnectionError. Please check your internet connection.")
    param = [{"operationAmount": {"amount": "47122.15", "currency": {"name": "USD.", "code": "USD"}}}]
    with pytest.raises(ConnectionError):
        get_conversion_apilayer(0, param)
