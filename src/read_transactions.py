import json

import pandas as pd
from pandas import DataFrame


def get_read_csv(path_to_file: str) -> str | list[dict]:
    """
    Считывание данных о финансовых операциях их CSV-файла
    :param path_to_file:
    :return:
    """
    try:
        data_transactions = pd.read_csv(path_to_file, delimiter=";")

    except FileNotFoundError as exc_info:
        return f"Function {get_read_csv.__name__} error: {type(exc_info).__name__}"
    except Exception as exc_info:
        return f"Error: {type(exc_info).__name__} - {str(exc_info)}"

    else:
        # return data_transactions.head().to_json(orient="records", indent=4, lines=True, force_ascii=False)
        return data_transactions.to_dict(orient="records")


def get_read_excel(path_to_file: str) -> str | list[dict]:
    """
    Считывание данных о финансовых операциях из файла Excel
    :param path_to_file:
    :return:
    """
    try:
        data_transactions = pd.read_excel(path_to_file)

    except FileNotFoundError as exc_info:
        return f"Function {get_read_excel.__name__} error: {type(exc_info).__name__}"
    except Exception as exc_info:
        return f"Error: {type(exc_info)} - {str(exc_info)}"

    else:
        return data_transactions.head().to_dict(orient="records")
        # return data_transactions.head().to_json(orient='records', indent=4, lines=True, force_ascii=False)


# trans = get_read_csv("../transactions.csv")
# print(trans)
# print(type(trans))
# print()
#
#
trans_1 = get_read_excel("../transactions_excel.xlsx")
print(trans_1)
# print(type(trans_1))
