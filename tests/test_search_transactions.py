import pytest

from src.search_transactions import get_search_transactions


@pytest.mark.parametrize(
    "value, string_search, expected",
    [
        (
            [
                {"amount": "79931.03", "currency": "RUB", "description": "Открытие вклада"},
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
            ],
            "организации",
            [{"amount": "31957.58", "code": "RUB", "description": "Перевод организации"}],
        ),
        (
            [
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
                {"amount": "8221.37", "code": "USD", "description": "Перевод со счета на счет"},
            ],
            "на счет",
            [{"amount": "8221.37", "code": "USD", "description": "Перевод со счета на счет"}],
        ),
        (
            [
                {"amount": "31957.58", "code": "RUB", "description": "Перевод организации"},
                {"amount": "8221.37", "code": "USD", "description": "Перевод со счета на счет"},
            ],
            "вклада",
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
        ),
        ([], "вклада", "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"),
    ],
)
def test_get_search_transactions(value: list[dict], string_search: str, expected: list[dict]) -> None:
    """
    Тестирование функции поиска словарей по заданной строке в описании транзакций
    :param value:
    :param string_search:
    :return:
    """
    assert get_search_transactions(value, string_search) == expected
