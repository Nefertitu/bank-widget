from unittest.mock import mock_open, patch

import pandas as pd

from src.read_transactions import get_read_csv, get_read_excel


def test_get_read_csv(data_for_test_csv: str, data_for_test_csv_result: list[dict]):
    """
    Проверяет, что функция читает CSV-файл и возвращает список словарей
    с данными о финансовых транзакциях
    :param data_for_test_csv:
    :param data_for_test_csv_result:
    :return:
    """
    mocked_open = mock_open(read_data=data_for_test_csv)
    with patch("builtins.open", mocked_open):
        result = get_read_csv("builtins.open")
        assert result == data_for_test_csv_result


def test_get_read_csv_invalid():
    """Проверяет, что функция читает файл и возвращает пустой словарь,
    если файл не содержит данных"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = get_read_csv("builtins.open")
        assert result == "Error: EmptyDataError - No columns to parse from file"


def test_get_read_csv_file_not_found():
    """Проверяет, что при отсутствии CSV-файла для чтения данных функция
    возвращает сведения об ошибке `FileNotFoundError`"""
    result = get_read_csv("test.csv")
    assert result == "Function get_read_csv error: FileNotFoundError"


@patch("pandas.read_excel")
def test_get_read_excel(mock_read_excel: pd.DataFrame):
    """
    Проверяет, что функция читает XLSX-файл и возвращает список словарей
    с данными о финансовых транзакциях
    :param mock_read_excel:
    :return:
    """

    sample_data = {"id": [650703, 3598919], "description": ["Перевод организации", "Перевод с карты на карту"]}
    mock_data = pd.DataFrame(sample_data)
    mock_read_excel.return_value = mock_data
    result = get_read_excel("sample")
    expected = [
        {"id": 650703, "description": "Перевод организации"},
        {"id": 3598919, "description": "Перевод с карты на карту"},
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_get_read_excel_invalid(mock_read_excel: pd.DataFrame):
    """
    Проверяет, что функция читает пустой XLSX-файл и возвращает пустой список
    :param mock_read_excel:
    :return:
    """
    mock_data = pd.DataFrame(None)
    mock_read_excel.return_value = mock_data
    result = get_read_excel("sample")
    expected = []
    assert result == expected


def test_get_read_excel_file_not_found():
    """Проверяет, что при отсутствии XLSX-файла для чтения данных функция
    возвращает сведения об ошибке `FileNotFoundError`"""
    result = get_read_excel("test.xlsx")
    assert result == "Function get_read_excel error: FileNotFoundError"
