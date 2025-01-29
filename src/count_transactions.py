from collections import Counter
from typing import Any

from src.utils import get_read_file



def get_count_transactions(data_transactions: list[dict], transactions_categories: list) -> Counter[Any]:
    """
    Подсчет количества банковских операций определенного типа
    :param filter_transactions:
    :param transactions_categories:
    :return:
    """
    descriptions = []
    for dict in data_transactions:
        if dict == {}:
            continue
        else:
            print(dict["description"])
            if dict["description"] is not None and (dict["description"]).lower() in transactions_categories:
                descriptions.append(dict["description"])
            else:
                continue
    counted = Counter(descriptions)

    return counted


trans = get_read_file('../data/operations.json')
print(trans)
print(len(trans))
trans_categories = ["перевод со счета на счет", "перевод с карты на карту", "открытие вклада"]
print(get_count_transactions(trans, trans_categories))
