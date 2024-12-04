from src.widget import get_date, mask_account_widget

if __name__ == "__main__":
    print(mask_account_widget("Visa Platinum 7000792289606361"))
    print()

    print(mask_account_widget("Счет 64686473678894779589"))
    print()

    print(get_date("2024-03-11T02:26:18.671407"))
