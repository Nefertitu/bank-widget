from typing import Any, Iterator, Union


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
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
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
# transactions = []

def filter_by_currency(list_dicts: list[dict[str, Any]], currency_type: str) -> Union[Iterator[list[dict[str, Any]]], str]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    выдающий поочередно транзакции, соответствующие заданной валюте"""
    filter_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_type, list_dicts))
    if list_dicts == []:
        yield "пустой список"
    else:

        for item in filter_transactions:
            if filter_transactions != None:
                yield item
        if filter_transactions == []:
            yield f"нет операций в валюте '{currency_type}'"


result_filter = filter_by_currency(transactions, "EUR")

while True:
    try:
        print(next(result_filter))

    except StopIteration:
        print("генератор исчерпан")
        break


# print(next(result_filter))
# print(next(result_filter))
# print(next(result_filter))
# print(next(result_filter))


def transactions_descriptions(list_dicts: list[dict[str, Any]]) -> Iterator[list[str]]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
        выдающий описание каждой операции по очереди"""

    list_descriptions = []

    if list_dicts == []:
        yield "пустой список"

    else:
        list_descriptions = list(dict["description"] for dict in list_dicts if dict.get("description") is not None)

        if list_descriptions != []:
            for item in list_descriptions:
             yield item

        else:
            yield "отсутствуют данные о проведенных операциях"


descriptions = transactions_descriptions(transactions)


for count in range(5):
    print(next(descriptions))
    count += 1

# while True:
#     try:
#         print(next(descriptions))
#     except StopIteration:
#         print("генератор исчерпан")
#         break


# def card_number_generator(start=0, stop=1):
#     """Функция генерирует номера банковских карт в заданном диапазоне
#     в формате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""
#
#     num = 10000000000000000
#     if stop != 0 and stop < 10000000000000000:
#
#         cards_numbers = (str((num + x)).lstrip("1") for x in range(start, stop + 1))
#         for number in cards_numbers:
#             yield f"{str(number[:4])} {str(number[4:8])} {str(number[8:12])} {str(number[12: ])}"
#
# for card_number in card_number_generator(10155,10157):
#     print(card_number)
