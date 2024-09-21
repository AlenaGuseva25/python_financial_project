from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирующая счет/карту"""
    if "Счет" in number:
        return f"{number[:-20]}{get_mask_account(number[-20:])}"
    else:
        return f"{number[:-16]}{get_mask_card_number(number[-16:])}"


def get_new_data(old_data: str) -> str:
    """Функция принимает строку и выводит дату в формате dd.mm.yyyy"""
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])
