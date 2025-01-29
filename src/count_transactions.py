from collections import Counter
from typing import Any


def get_count_transactions(data_transactions: list[dict], transactions_categories: list) -> Counter[Any] | str:
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
            if dict["description"] is not None and (dict["description"]).lower() in transactions_categories:
                descriptions.append(dict["description"])
            else:
                continue
    counted = Counter(descriptions)

    return counted


# trans = get_read_file("../data/operations.json")
trans = [{"amount": "79931.03", "currency": "RUB", "description": "Открытие вклада"},
         {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"}]
trans_categories = ["перевод организации", "открытие вклада"]
print(get_count_transactions(trans, trans_categories))
