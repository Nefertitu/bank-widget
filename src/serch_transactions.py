import re

from src.read_transactions import  get_read_csv


def get_search_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Поиск транзакций с данными о банковских операциях по строке поиска
    :param transactions:
    :param search_string:
    :return:
    """
    found_transactions = []

    for dict in transactions:
        if dict == {}:
            continue
        pattern = f"{search_string}"
        match = re.search(pattern, str(dict['description']), flags=re.IGNORECASE)
        if match:
            found_transactions.append(dict)
        else:
            continue
    return found_transactions


# trans_for_search = get_read_excel("../transactions_excel.xlsx")
trans_for_search = trans = get_read_csv("../transactions.csv")
# trans_for_search = get_read_file('../data/operations.json')
# print(trans_for_search)
result = get_search_transactions(trans_for_search, 'вклада')
print(len(result))
print(result)

