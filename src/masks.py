def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :param card_number:
    :return:
    """

    number = str(card_number)
    star = "*"
    if 13 <= len(number) <= 19 and len(number) != 14 and len(number) != 17 and number.isdigit() is True:
        mask_number = f"{number[:4]} {number[4:6]}** {star * (len(number) - 12)} {number[-4:]}"
        return mask_number
    if len(number) == 0:
        return "пустой ввод"
    else:
        return "некорректный ввод данных"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску
    :param account_number:
    :return:
    """

    account = str(account_number)
    if len(account) == 20 and account.isdigit() is True:
        mask_account = f"**{account[16:]}"
        return mask_account
    if len(account) == 0:
        return "пустой ввод"
    if 20 > len(account) > 0 or len(account) > 20 or account.isdigit() is False:
        return "некорректный ввод данных"

    return ""
