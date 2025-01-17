import os
import random
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apilayer_key = os.getenv("API_KEY")


def get_conversion_apilayer(random_number: int, data_transactions: Any | list[dict[Any, Any]]) -> Any:
    """
    Принимает на вход список транзакций, возвращает сумму транзакции, выбранной
    рандомно, в рублях. Если выбранная транзакция проведена не в рублях,
    осуществляет конвертацию суммы транзакции в рубли, обращаясь к сайту:
    'https://api.apilayer.com/'
    :param random_number:
    :param data_transactions:
    :return:
    """
    for _ in data_transactions:
        random_transaction = data_transactions[random_number]
        try:
            currency_code = random_transaction["operationAmount"]["currency"]["code"]
            amount = round(float(random_transaction["operationAmount"]["amount"]), 2)

        except KeyError as exc_info:
            return f"Error: {type(exc_info).__name__}, {str(exc_info)}"
        except ValueError as exc_info:
            return f"Error: {type(exc_info).__name__}, {str(exc_info)}"
        except TypeError as exc_info:
            return f"Error: {type(exc_info).__name__}, {str(exc_info)}"

        else:
            if currency_code == "RUB":
                return f"Сумма транзакции составляет {amount} {currency_code}."

            elif currency_code == "USD" or currency_code == "EUR":
                headers = {"apikey": f"{apilayer_key}"}
                try:
                    response = requests.get(
                        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&"
                        f"amount={amount}",
                        headers=headers,
                        data={},
                        timeout=5,
                    )
                    status_code = response.status_code
                    response.raise_for_status()

                except requests.exceptions.Timeout:
                    return "Request timed out. Please check your internet connection."

                except requests.exceptions.ConnectionError:
                    return "ConnectionError. Please check your internet connection."

                except requests.exceptions.HTTPError:
                    return "HTTP Error. Please check the URL."

                else:

                    if status_code == 200:
                        return (
                            f"Сумма транзакции составляет {response.json()['query']['amount']} "
                            f"{response.json()['query']['from']} "
                            f"или {round(response.json()['result'], 2)} рублей "
                            f"в соответствии с текущим курсом валют на дату: {response.json()['date']}."
                        )

                    return response.json()

            return "Неверный код валюты"


def get_random_number(transactions: list[dict[Any, Any]]) -> int | str:
    """
    Возвращает рандомный номер или '1'
    :param transactions:
    :return:
    """
    if len(transactions) > 1:
        return random.randint(0, len(transactions) - 1)
    elif len(transactions) == 1:
        return 1
    return "Список не должен быть пустым"


def data_for_test_rub() -> list[dict[Any, Any]]:
    """
    Возвращает список словарей с данными о транзакциях,
    проведенных в рублях
    :return:
    """

    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "55149.24", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
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
    ]
