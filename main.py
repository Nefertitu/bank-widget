from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import get_read_csv, get_read_excel
from src.search_transactions import get_search_transactions
from src.utils import get_read_file
from src.widget import get_date, mask_account_card


def main() -> str:
    """Функция отвечает за основную логику проекта и связывает функциональности
    проекта между собой"""
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    transactions: list[dict] = []
    answer = ["1", "2", "3"]
    answer_file = input(
        (
            """Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
: """
        )
    )
    while answer_file not in answer:
        answer_file = input(
            (
                """Выберите один из пунктов меню ниже:
                       1. Получить информацию о транзакциях из JSON-файла
                       2. Получить информацию о транзакциях из CSV-файла
                       3. Получить информацию о транзакциях из XLSX-файла
: """
            )
        )
    if answer_file == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_read_file("./data/operations.json")
    if answer_file == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = get_read_csv("./transactions.csv")  # type: ignore
    if answer_file == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = get_read_excel("./transactions_excel.xlsx")  # type: ignore

    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    if answer_file == "2" or answer_file == "3":
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.")
    elif answer_file == "1":
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED.")

    answer = ["EXECUTED", "CANCELED", "PENDING"]
    answer_status = (input()).upper()
    while answer_status not in answer:
        print("\nВведите один из доступных статусов для фильтровки.")
        answer_status = (input()).upper()

    transactions = filter_by_state(transactions, answer_status)
    print(f"\nОперации отфильтрованы по статусу '{answer_status}'.")

    print("\nОтсортировать операции по дате? Да/Нет")
    answer = ["да", "нет"]
    answer_sort_date = (input()).lower()
    while answer_sort_date not in answer:
        print("\nЧтобы отсортировать операции по дате наберите 'Да' или 'Нет'")
        answer_sort_date = (input()).lower()
    if answer_sort_date.lower() == "да":
        print("\nОтсортировать по возрастанию или по убыванию?")
        answer = ["по возрастанию", "по убыванию"]
        answer_sort_order = (input()).lower()
        while answer_sort_order not in answer:
            print("\nНаберите: 'по возрастанию' или 'по убыванию'.")
            answer_sort_order = (input()).lower()
            if answer_sort_order.lower() == "по возрастанию":
                transactions = sort_by_date(transactions, sort_order=False)
            if answer_sort_date.lower() == "по убыванию":
                transactions = sort_by_date(transactions, sort_order=True)
    if answer_sort_date.lower() == "нет":
        transactions = transactions

    print("\nВыводить только рублевые транзакции? Да/Нет")
    answer = ["да", "нет"]
    answer_currency = (input()).lower()
    while answer_currency not in answer:
        print("\nВыводить только рублевые транзакции? Наберите 'Да' или 'Нет'.")
        answer_currency = (input()).lower()
    if answer_currency.lower() == "да":
        transactions = filter_by_currency(transactions, "RUB")
    if answer_currency.lower() == "нет":
        transactions = transactions

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer = ["да", "нет"]
    answer_description = (input()).lower()
    while answer_description not in answer:
        print("\nНаберите 'Да' или 'Нет', чтобы отфильтровать список транзакций.")
        answer_description = (input()).lower()
    if answer_description.lower() == "да":
        print(
            """\nВведите слово или фразу для поиска в описании транзакций (перевод с карты
на карту, перевод со счета на счет, открытие вклада, перевод организации.)"""
        )
        answer = [
            "перевод с карты",
            "перевод с карты на карту",
            "перевод со счета",
            "перевод со счета на счет",
            "перевод организации",
            "открытие вклада",
            "перевод",
            "со счета",
            "на счет",
            "счет",
            "на карту",
            "карту",
            "открытие",
            "вклада",
            "организации",
        ]
        answer_serch_string = (input()).lower()
        transactions = get_search_transactions(transactions, answer_serch_string)  # type: ignore

        x = 0
        while answer_serch_string not in answer and x < 3:
            print(
                """\nВведите слово или фразу для поиска в описании транзакций
из приведенного выше списка."""
            )
            answer_serch_string = (input()).lower()
            x += 1
            if x == 3 and answer_serch_string not in answer:
                print("Не удалось выполнить фильтрацию по описанию.")

            if x < 3 and answer_serch_string in answer:
                transactions = get_search_transactions(transactions, answer_serch_string)  # type: ignore
            else:
                transactions = get_search_transactions(transactions, answer_serch_string)  # type: ignore

    if answer_description.lower() == "нет":
        transactions = transactions

    print("\nРаспечатываю итоговый список транзакций...\n")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(list(transactions))}\n")
        for transaction in transactions:
            if transaction.get("date") is None:
                continue
            else:
                print(f'{get_date(str(transaction["date"]))} {transaction["description"]}')
                if transaction["description"] == "Открытие вклада":
                    print(f'{mask_account_card(transaction["to"])}')
                    if transaction.get("operationAmount") is None:
                        print(f'Сумма: {transaction["amount"]} {transaction["currency_code"]}\n')
                    else:
                        print(
                            f"""Сумма: {transaction["operationAmount"].get("amount")}
{transaction["operationAmount"].get("currency").get("code")}\n"""
                        )
                else:
                    print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
                    if transaction.get("operationAmount") is None:
                        print(f"Сумма: {transaction["amount"]} {transaction["currency_code"]}\n")
                    else:
                        print(
                            f"""Сумма: {transaction["operationAmount"].get("amount")}
{transaction["operationAmount"].get("currency").get("code")}\n"""
                        )

    if transactions is None:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    return ""


if __name__ == "__main__":
    print(main())
