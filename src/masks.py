import logging

root_logger = logging.getLogger()
logger = logging.getLogger("masks")
file_handler = logging.FileHandler("./logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску,
    логирует результаты выполнения функции в файл
    :param card_number:
    :return:
    """
    logger.info(f'\nПолучен номер карты для маскировки - "{card_number}"')
    number = str(card_number)
    star = "*"
    if 13 <= len(number) <= 19 and len(number) != 14 and len(number) != 17 and number.isdigit() is True:
        mask_number = f"{number[:4]} {number[4:6]}** {star * (len(number) - 12)} {number[-4:]}"
        logger.info(f"\nУспешно выполнена маскировка номера карты - {mask_number}")
        return mask_number
    if len(number) == 0:
        logger.warning("Пустой ввод")
        return "пустой ввод"
    else:
        logger.error(
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
    logger.info(f'\nПолучен номер счета для маскировки - "{account_number}"')
    account = str(account_number)
    if len(account) == 20 and account.isdigit() is True:
        mask_account = f"**{account[16:]}"
        logger.info(f"\nУспешно выполнена маскировка номера счета - {mask_account}")
        return mask_account
    if len(account) == 0:
        logger.warning("Пустой ввод")
        return "пустой ввод"
    if len(account) != 20 or account.isdigit() is False:
        logger.error(
            f"\nПолучены некорректные данные, так как длина введенного номера "
            f"\nсчета не соответствует установленным параметрам количества "
            f"\nсимволов номера счета - 20, и составляет {len(account)}."
        )
        return "некорректный ввод данных"

    return ""


def main_card_1() -> tuple[str, str, str]:
    """Логирует тесты(№№1 - 3) функции `get_mask_card_number()`"""
    logger.info("\nЗапуск приложения c тестовыми данными")
    logger.info("\nТест_№1")
    result_1 = get_mask_card_number("")
    logger.info("\nТест_№2")
    result_2 = get_mask_card_number("123456789")
    logger.info("\nТест_№3")
    result_3 = get_mask_card_number("123456789456123789")
    logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2, result_3


def main_account_1() -> tuple[str, str, str]:
    """Логирует тесты(№№1 - 3) функции `get_mask_account()`"""
    logger.info("\nЗапуск приложения с тестовыми данными")
    logger.info("\nТест_№1")
    result_1 = get_mask_account("")
    logger.info("\nТест_№2")
    result_2 = get_mask_account("123456789123")
    logger.info("\nТест_№3")
    result_3 = get_mask_account("12345678912345678912")
    logger.info("\nЗавершение работы приложения\n\n")
    return result_1, result_2, result_3
