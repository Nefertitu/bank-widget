from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    number = str(card_number)
    mask_number = f"{number[:4]} {number[4:6]}** **** {number[12:]}"
    return mask_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    account = str(account_number)
    mask_account = f"**{account[16:]}"
    return mask_account
