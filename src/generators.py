from typing import Any, Generator


def filter_by_currency(list_dicts: list[dict[str, Any]], currency_type: str) -> Any:
    """
    Функция принимает список словарей с транзакциями и возвращает итератор,
    выдающий поочередно транзакции, соответствующие заданной валюте
    :param list_dicts:
    :param currency_type:
    :return:
    """

    filter_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_type, list_dicts))

    if list_dicts == []:
        yield "пустой список"
    else:

        for item in filter_transactions:
            if filter_transactions is not None:
                yield item
        if filter_transactions == []:
            yield f"нет операций в валюте '{currency_type}'"

    return ""


# print(next(result_filter))
# print(next(result_filter))
# print(next(result_filter))
# print(next(result_filter))


def transactions_descriptions(list_dicts: list[dict[str, Any]]) -> Any:
    """
    Функция принимает список словарей с транзакциями и возвращает итератор,
    выдающий описание каждой операции по очереди
    :param list_dicts:
    """

    list_descriptions = []

    if list_dicts == []:
        yield "пустой список"

    else:
        list_descriptions = list(dict["description"] for dict in list_dicts if dict.get("description") is not None)

        if list_descriptions != []:
            for item in list_descriptions:
                yield item

        else:
            yield "отсутствуют данные о проведенных операциях"

    return ""


# while True:
#     try:
#         print(next(descriptions))
#     except StopIteration:
#         print("генератор исчерпан")
#         break


def card_number_generator(start: int = 1, stop: int = 1) -> Generator[list[str]] | str:
    """
    Функция генерирует номера банковских карт в заданном диапазоне
    в формате 'ХХХХ ХХХХ ХХХХ ХХХХ'
    :param start:
    :param stop:
    :return:
    """

    num = 10**16

    if type(start) is int and type(stop) is int:

        if num > start != 0 and num > stop != 0:

            if start > stop:
                cards_numbers = (str((num + x)).lstrip("1") for x in range(stop, start + 1))
                for number in cards_numbers:
                    yield f"{str(number[:4])} {str(number[4:8])} {str(number[8:12])} {str(number[12:])}"

            if stop > start:

                cards_numbers = (str((num + x)).lstrip("1") for x in range(start, stop + 1))
                for number in cards_numbers:
                    yield f"{str(number[:4])} {str(number[4:8])} {str(number[8:12])} {str(number[12:])}"

            if stop == num - 1 or start == num - 1:
                yield "!!!доcтигнуто предельное значение номера карты - '9999 9999 9999 9999'!!!"

        else:
            yield "номер карты не может быть равным '0' и не должен превышать '9999 9999 9999 9999'"

    else:
        yield "Ошибка: некорректный ввод"

    return ""
