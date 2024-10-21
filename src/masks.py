import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("masks.log")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# entering_the_account_number = input("Enter your entering account number: ")
# entering_the_card_number = input("Enter the card number: ")


def get_mask_card_number(entering_the_card_number: str) -> str:
    """Функция возвращающая маску карты"""
    if len(entering_the_card_number) != 16 or not entering_the_card_number.isdigit():
        logger.error("Некорректный номер карты. Должно быть 16 цифр.")
        return "Некорректный номер карты"
    masked_card = (
        f"{entering_the_card_number[:4]} {entering_the_card_number[4:6]}** **** {entering_the_card_number[12:]}"
    )
    logger.info(f"Создана маска карты: {masked_card}")
    return masked_card


def get_mask_account(entering_the_account_number: str) -> str:
    """Функция возвращающая маску счета"""
    if len(entering_the_account_number) < 20 or not entering_the_account_number.isdigit():
        logger.error("Некорректный номер счета. Должен содержать как минимум 20 цифр")
        return "Некорректный номер счета"
    masked_account = f"**{entering_the_account_number[-4:]}"
    logger.info(f"Создана маска счета: {masked_account}")
    return masked_account


if __name__ == "__main__":
    card_result = get_mask_card_number("1234567812345678")
    print(f"Маска карты: {card_result}")
