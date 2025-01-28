from decorators import my_function
from src.external_api import main_rub
from src.generators import card_number_generator, filter_by_currency, transactions_descriptions
from src.masks import main_account_1, main_card_1
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import get_read_csv, get_read_excel
from src.serch_transactions import get_search_transactions
from src.utils import main_read_1, main_read_2, main_read_3, get_read_file
from src.widget import get_data, mask_account_card

if __name__ == "__main__":

    print(mask_account_card("Visa Platinum 7000792289606361"))
    print()

    print(mask_account_card("Счет 64686473678894779589"))
    print()

    print(get_data("2024-03-11T02:26:18.671407"))
    print()

    transaction_list = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    print(filter_by_state(transaction_list, state="CANCELED"))
    print()

    transaction_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    print(sort_by_date(transaction_list, sort_order=False))
    print()

    transactions = [
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

    result_filter = filter_by_currency(transactions, "EUR")

    while True:
        try:
            print(next(result_filter))

        except StopIteration:
            print("генератор исчерпан")
            print()
            break

    descriptions = transactions_descriptions(transactions)

    for count in range(5):
        print(next(descriptions))
        count += 1

    print()

    for card_number in card_number_generator(5, 1):
        print(card_number)
        print()

    print(my_function(1, 2))
    print(my_function(1, "5"))
    print(my_function(1, 0))
    print()


    # print(main_api())
    # print()

    print(main_rub())
    print()

    print(main_card_1())
    print()

    print(main_account_1())
    print()

    print(main_read_1())
    print(main_read_2())
    print(main_read_3())
    print()

    print(get_read_csv("./transactions.csv"))
    print()

    data_transactions = get_read_excel("./transactions_excel.xlsx")
    for dict in data_transactions:
        print(dict)


def get_file():
    answer_file = input()
    if answer_file == "1":
        print("Для обработки выбран JSON-файл.")
        return get_read_file('./data/operations.json')
    if answer_file == "2":
        print("Для обработки выбран CSV-файл.")
        return get_read_csv("./transactions.csv")
    if answer_file == "3":
        print("Для обработки выбран XLSX-файл.")
        return get_read_excel("./transactions_excel.xlsx")
    else:
        return "Не выбран ни один из вариантов"


def get_sort_order_by_date(answer_sort_date):
    if answer_sort_date.lower() == "да":
        return False
    return True

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print("""Выберите необходимый пункт меню:\n
        1. Получить информацию о транзакциях из JSON-файла\n
        2. Получить информацию о транзакциях из CSV-файла\n
        3. Получить информацию о транзакциях из XLSX-файла"\n
        """)
    transaction_file = get_file()

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n")
    answer_status = input()
    transactions_sort_status = filter_by_state(transaction_file, answer_status)
    print(f"Операции отфильтрованы по статусу '{answer_status}'.\n")

    print("Отсортировать операции по дате? Да/Нет\n")
    answer_sort_date = input()

    if answer_sort_date.lower() == "да":
    print("Отсортировать по возрастанию или по убыванию?\n")
    answer_sort_order = input()
    if answer_sort_order.lower() == "по возрастанию":
        transactions_sort_by_date = sort_by_date(transactions_sort_status, sort_order=False)
    if answer_sort_date.lower() == "по убыванию":
        transactions_sort_by_date = sort_by_date(transactions_sort_status)
    if answer_sort_date.lower() == "нет":
        transactions_sort_by_date = transactions_sort_status

    print("Выводить только рублевые транзакции? Да/Нет\n")
    answer_currency = input()
    if answer_currency.lower() == "да":
        transactions_filtered_currency = filter_by_currency(transactions_sort_by_date, "RUB")
    if answer_currency.lower() == "нет":
        transactions_filtered_currency = transactions_sort_by_date

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    answer_description = input()
    if answer_description.lower() == "да":
        transactions_filter_descriptions = transactions_descriptions(transactions_filtered_currency)
    if answer_description.lower() == "нет":
        transactions_filter_descriptions = transactions_filtered_currency

    print("Распечатываю итоговый список транзакций...")

