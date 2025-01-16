import os
import random

from dotenv import load_dotenv
import requests

load_dotenv()
apilayer_key = os.getenv('API_KEY')


def get_conversion_apilayer(random_number: int, transactions_test: list[dict]) ->  str | float| None :
    """
    Принимает на вход список транзакций, возвращает сумму транзакции, выбранной
    рандомно, в рублях. Если выбранная транзакция проведена не в рублях,
    осуществляет конвертацию суммы транзакции в рубли, обращаясь к сайту:
    'https://api.apilayer.com/'
    :param random_number:
    :param transactions_test:
    :return:
    """

    for _ in transactions_test:
        random_transaction = transactions_test[random_number]
        currency = random_transaction['operationAmount']['currency']['code']
        amount = round(float(random_transaction['operationAmount']['amount']), 2)

        if currency is not None:

            if currency == 'RUB':
                return f'Сумма транзакции составляет {amount} {currency}.'

            else:

                headers = {"apikey": f'{apilayer_key}'}

                try:
                    response = requests.get(
                            f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}',
                            headers=headers, data={}, timeout=10)
                    response.raise_for_status()

                except requests.exceptions.Timeout:
                    return "Request timed out. Please check your internet connection."

                except requests.exceptions.ConnectionError:
                    return "Connection Error. Please check your network connection."

                except requests.exceptions.HTTPError:
                    return "HTTP Error. Please check the URL."

                else:

                    if response.json():
                        return (f'Сумма транзакции составляет {response.json()['query']['amount']} {response.json()['query']['from']} '
                                f'или {round(response.json()['result'], 2)} рублей '
                                f'в соответствии с текущим курсом валют на дату: {response.json()['date']}.')

                    return response.json()
                # response = requests.get(
                #         f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}',
                #         headers=headers, data={})
                # if response.json()['result']:
                #     return f'Сумма транзакции составляет {amount} {currency} или {round(response.json()['result'], 2)} рублей в соответствии с текущим (дата: {response.json()['date']}) курсом валют.'
                # return 'You have exceeded your daily\/monthly API rate limit'

        return 'Нет данных'


transactions_test = [
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
  },
{
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
{
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }
]


def get_random_number(transactions):
    if len(transactions) > 1:
        return random.randint(0,len(transactions) - 1)
    return 1


random_number = get_random_number(transactions_test)
# transactions_test = get_read_file(path_to_file)
print(get_conversion_apilayer(random_number, transactions_test))
# print(len(transactions_test))



