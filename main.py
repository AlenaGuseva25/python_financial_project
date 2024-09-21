# from src.masks import get_mask_account
#
# from src.masks import get_mask_card_number
#
# print(get_mask_account("73654108430135874305"))
# print(get_mask_card_number("7000792289606361"))

from src.widget import mask_account_card

from src.widget import get_new_data

print(mask_account_card("Счет 64686473678894779589"))
print(get_new_data("2024-04-11T02:26:18.671407"))
