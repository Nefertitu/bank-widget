import os
from dotenv import load_dotenv
import requests

load_dotenv()
apilayer_key = os.getenv('API_KEY')


def get_transactions(currency: str, amount: int | float) -> float | str | None:
    """
    Конвертация суммы транзакции, выполненной в USD или EUR, в рубли
    с сайта 'https://api.apilayer.com/'
    :param currency:
    :param amount:
    :return:
    """

    try:
        response = requests.get('https://api.apilayer.com')

    except requests.exceptions.ConnectionError:
        return "Connection Error. Проверьте сетевое подключение."

    else:

        if currency == 'USD' or currency == 'EUR':

            headers = {
      "apikey": f'{apilayer_key}'
    }
            response = requests.get(
                    f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}',
                    headers=headers, data={})
            return f'Сумма транзакции составляет {amount} {currency} или {round(response.json()['result'], 2)} рублей по курсу конвертации валют на дату: {response.json()['date']}.'

    return 'Выберете для конвертации USD или EUR'


print(get_transactions('EUR', 15))



