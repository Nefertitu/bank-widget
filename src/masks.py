def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    number = str(card_number)
    star = "*"
    if 13 <= len(number) > 0 and number.isdigit() is True:
        mask_number = f"{number[:4]} {number[4:6]}** {star * (len(number) - 12)} {number[-4:]}"
        return mask_number
    if len(number) == 0:
        return "пустой ввод"
    else:
        return "введены некорректные данные"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    account = str(account_number)
    if len(account) == 20 and account.isdigit() is True:
        mask_account = f"**{account[16:]}"
        return mask_account
    if len(account) == 0:
        return "пустой ввод"
    return "введены некорректные данные"


# print(get_mask_account(""))