

entering_the_account_number = input("Enter your entering account number: ")
entering_the_card_number = input("Enter the card number: ")


def get_mask_card_number(entering_the_card_number: str) -> str:
    """Функция, возвращающая маску карты"""
    return f"{entering_the_card_number[:4]}{entering_the_card_number[4:6]}** **** {entering_the_card_number[12:]}"


def get_mask_account(entering_the_account_number: str) -> str:
    """Функция, возвращающая маску счета"""
    return f"**{entering_the_account_number[-4:]}"


print(get_mask_card_number(entering_the_account_number))
print(get_mask_account(entering_the_card_number))
