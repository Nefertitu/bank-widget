from unittest.mock import mock_open, patch

from src.utils import get_read_file, main_read_1, main_read_2, main_read_3


def test_get_read_file_success(data_for_test_1):
    """Проверяет, что функция читает файл и возвращает список словарей
    с данными о финансовых транзакциях"""

    mocked_open = mock_open(read_data=data_for_test_1)
    with patch("builtins.open", mocked_open):
        result = get_read_file("builtins.open")
        assert result == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]


def test_get_read_file_invalid():
    """Проверяет, что функция читает файл и возвращает пустой словарь,
    если файл не содержит данных"""
    mocked_open = mock_open(read_data=None)
    with patch("builtins.open", mocked_open):
        result = get_read_file("builtins.open")
        assert result == []


def test_get_read_file_decode_error_console(capsys):
    """Проверяет вывод в консоль ошибки `JSONDecodeError`, если невозможно
    декодировать (преобразовать) JSON-данные, содержащиеся в файле"""
    param = "[{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}"
    mocked_open = mock_open(read_data=param)
    with patch("builtins.open", mocked_open):
        print(get_read_file("builtins.open"))
        captured = capsys.readouterr()
        assert captured.out == "JSONDecodeError: Invalid JSON data.\n[]\n"


def test_get_read_file_decode_error_return():
    """Проверяет, что функция возвращает пустой список, если возникает ошибка
    `JSONDecodeError`, когда невозможно декодировать (преобразовать) JSON-данные,
    содержащиеся в файле"""
    param = "[{'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}"
    mocked_open = mock_open(read_data=param)
    with patch("builtins.open", mocked_open):
        result = get_read_file("builtins.open")
        assert result == []


def test_get_read_file_not_found_console(capsys):
    """Проверяет, что при отсутствии файла для чтения данных выдается
    соответствующее сообщение в консоль"""
    print(get_read_file("test.json"))
    captured = capsys.readouterr()
    assert captured.out == "FileNotFoundError: Файл не найден.\n[]\n"


def test_get_read_file_not_found_return():
    """Проверяет, что при отсутствии файла для чтения данных функция
    возвращает пустой список"""
    result = get_read_file("test.json")
    assert result == []


def test_main_read_1_console(capsys):
    """Проверяет, что при отсутствии JSON-файла для чтения выводится соответствующее
    сообщение в консоль"""
    print(main_read_1())
    captured = capsys.readouterr()
    assert captured.out == "FileNotFoundError: Файл не найден.\n[]\n"


def test_main_read_2():
    """Проверяет, что функция возвращает список словарей с данными, полученными из JSON-файла
    содержащиеся в файле"""
    param = '[{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]'
    mocked_open = mock_open(read_data=param)
    with patch("builtins.open", mocked_open):
        result = main_read_2()
        assert result == [{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]


def test_main_read_3_console(capsys):
    """Проверяет, что при чтении JSON-файла с некорректными данными выводится
    соответствующее сообщение в консоль"""
    print(main_read_3())
    captured = capsys.readouterr()
    assert captured.out == "JSONDecodeError: Invalid JSON data.\n[]\n"
