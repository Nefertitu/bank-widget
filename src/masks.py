import logging

root_logger = logging.getLogger()
mask_card_logger = logging.getLogger("app.mask_card")
mask_account_logger = logging.getLogger("app.mask_account")
main_logger = logging.getLogger("app.main")
file_handler = logging.FileHandler("./logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
mask_card_logger.addHandler(file_handler)
mask_account_logger.addHandler(file_handler)
main_logger.addHandler(file_handler)
mask_card_logger.setLevel(logging.DEBUG)
mask_account_logger.setLevel(logging.DEBUG)
main_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску,
    логирует результаты выполнения функции в файл
    :param card_number:
    :return:
    """
    mask_card_logger.info(f'\nПолучен номер карты для маскировки - "{card_number}"')
    number = str(card_number)
    star = "*"
    if 13 <= len(number) <= 19 and len(number) != 14 and len(number) != 17 and number.isdigit() is True:
        mask_number = f"{number[:4]} {number[4:6]}** {star * (len(number) - 12)} {number[-4:]}"
        mask_card_logger.info(f"\nУспешно выполнена маскировка номера карты - {mask_number}")
        return mask_number
    if len(number) == 0:
        mask_card_logger.warning("Пустой ввод")
        return "пустой ввод"
    else:
        mask_card_logger.error(
            f"\nПолучены некорректные данные, так как длина введенного номера "
            f"\nкарты не соответствует установленным параметрам количества "
            f"\nсимволов номера карты (13, 15, 16, 18 и 19) и составляет {len(card_number)}."
        )
        return "некорректный ввод данных"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску,
    логирует результаты выполнения функции в файл
    :param account_number:
    :return:
    """
    mask_account_logger.info(f'\nПолучен номер счета для маскировки - "{account_number}"')
    account = str(account_number)
    if len(account) == 20 and account.isdigit() is True:
        mask_account = f"**{account[16:]}"
        mask_account_logger.info(f"\nУспешно выполнена маскировка номера счета - {mask_account}")
        return mask_account
    if len(account) == 0:
        mask_account_logger.warning("Пустой ввод")
        return "пустой ввод"
    if len(account) != 20 or account.isdigit() is False:
        mask_account_logger.error(
            f"\nПолучены некорректные данные, так как длина введенного номера "
            f"\nсчета не соответствует установленным параметрам количества "
            f"\nсимволов номера счета - 20, и составляет {len(account)}."
        )
        return "некорректный ввод данных"

    return ""


def main_card_1() -> tuple[str, str, str]:
    """Логирует тесты(№№1 - 3) функции `get_mask_card_number()`"""
    main_logger.info("\nЗапуск приложения c тестовыми данными")
    main_logger.info("\nТест_№1")
    result_1 = get_mask_card_number("")
    main_logger.info("\nТест_№2")
    result_2 = get_mask_card_number("123456789")
    main_logger.info("\nТест_№3")
    result_3 = get_mask_card_number("123456789456123789")
    main_logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2, result_3


def main_card_2() -> tuple[str, str, str]:
    """Логирует тесты(№№1 - 3) функции `get_mask_card_number()`"""
    main_logger.info("\nЗапуск приложения c тестовыми данными")
    main_logger.info("\nТест_№1")
    result_1 = get_mask_card_number("")
    main_logger.info("\nТест_№2")
    result_2 = get_mask_card_number("220002021725")
    main_logger.info("\nТест_№3")
    result_3 = get_mask_card_number("2200020217251111")
    main_logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2, result_3


def main_account_1() -> tuple[str, str, str]:
    """Логирует тесты(№№1 - 3) функции `get_mask_account()`"""
    main_logger.info("\nЗапуск приложения с тестовыми данными")
    main_logger.info("\nТест_№1")
    result_1 = get_mask_account("")
    main_logger.info("\nТест_№2")
    result_2 = get_mask_account("123456789123")
    main_logger.info("\nТест_№3")
    result_3 = get_mask_account("12345678912345678912")
    main_logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2, result_3


def main_account_2() -> tuple[str, str]:
    """Логирует тесты(№1, №2) функции `get_mask_account()`"""
    main_logger.info("\nЗапуск приложения с тестовыми данными")
    main_logger.info("\nТест_№1")
    result_1 = get_mask_account("9999999999999")
    main_logger.info("\nТест_№2")
    result_2 = get_mask_account("99999999999999999999")
    main_logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2
