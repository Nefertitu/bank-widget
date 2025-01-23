from unittest.mock import mock_open, patch

from src.read_transactions import get_read_csv
from tests.conftest import data_for_test_csv_result


def test_get_read_transactions_csv(data_for_test_csv: str, data_for_test_csv_result: list[dict]):
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


def test_get_read_transactions_csv_invalid():
    """Проверяет, что функция читает файл и возвращает пустой словарь,
    если файл не содержит данных"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = get_read_csv("builtins.open")
        assert result == "Error: EmptyDataError - No columns to parse from file"


def test_get_read_transactions_file_not_found():
    """Проверяет, что при отсутствии CSV-файла для чтения данных функция
    возвращает сведения об ошибке `FileNotFoundError`"""
    result = get_read_csv("test.csv")
    assert result == "Function get_read_csv error: FileNotFoundError"
