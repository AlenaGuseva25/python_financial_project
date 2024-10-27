import os
from _datetime import datetime

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_new_data
from src.processing import sort_by_date, filter_by_state
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.utils import financial_transactions
from src.external_api import convert_to_rub
from src.reading_data_csv_excel import reader_file_transaction_csv, reader_file_transaction_excel
from src.dictonary_search import search_transactions, count_transactions

json_file = financial_transactions("../data/operations.json")
csv_file = reader_file_transaction_csv("../data/transactions.csv")
excel_file = reader_file_transaction_excel("../data/transactions_excel.xlsx")


def main():
    """Отвечает за основную логику проекта с пользователем,
    связывает функциональности между собой."""

    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_input_file = input("Введите номер пункта: ")

    if user_input_file == "1":
        json_file = financial_transactions("../data/operations.json")
        print("Для обработки выбран JSON-файл.")
        transactions_from_file = json_file
    elif user_input_file == "2":
        csv_file = reader_file_transaction_csv("../data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
        transactions_from_file = csv_file
    elif user_input_file == "3":
        excel_file = reader_file_transaction_excel("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
        transactions_from_file = excel_file
    else:
        print("Введен некорректный номер.")
        return

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_state = input("Введите статус для фильтрации: ").upper()
        if user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {user_state} недоступен.")
            continue
        print(f"Операции отфильтрованы по статусу {user_state}")
        filter_state = filter_by_state(transactions_from_file, user_state)
        break

    print("Отсортировать операции по дате? Да/Нет")
    user_date = input("Введите да или нет ").lower()
    if user_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_up_down = input("в порядке убывания / в порядке возрастания ").lower()
        if user_input_up_down == "в порядке убывания":
            reversed = True
            filter_transaction_date = sort_by_date(filter_state, reversed)
        elif user_input_up_down == "в порядке возрастания":
            reversed = False
            filter_transaction_date = sort_by_date(filter_state, reversed)
        else:
            print("Введен некорректный ответ.")
            return
    elif user_date == "нет":
        filter_transaction_date = filter_state
    else:
        print("Введен некорректный ответ.")
        return

    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_curr = input("Введите да или нет: ").lower()
    rub_trans = []
    if user_input_curr == "да":
        for trans in filter_transaction_date:
            if (user_input_file == "1" or user_input_file == "2") and trans["operationAmount"]["currency"][
                "code"] == "RUB":
                rub_trans.append(trans)
            elif user_input_file == "3" and trans["currency_code"] == "RUB":
                rub_trans.append(trans)
    elif user_input_curr == "нет":
        rub_trans = filter_transaction_date
    else:
        print("Введен некорректный ответ.")
        return

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_word = input("Введите да или нет: ").lower()
    trans_word = []
    if sort_by_word == "да":
        sort_by_word_yes = input("Введите слово для фильтрации: ")
        for trans in rub_trans:
            if sort_by_word_yes in trans["description"]:
                trans_word.append(trans)
    elif sort_by_word == "нет":
        trans_word = rub_trans
    else:
        print("Введен некорректный ответ.")
        return

    if len(trans_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans_word)}\n")

    for trans in trans_word:
        date = trans.get("date", "")[:19]
        bad_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        correct_date = bad_date.strftime("%d.%m.%Y")
        description = trans.get("description", "")
        masked_card_from = get_mask_card_number(str(trans.get("from")))
        masked_card_to = get_mask_card_number(str(trans.get("to")))
        amount = trans.get("operationAmount", {}).get("amount", trans.get("amount", 0))

        if user_input_file == "1":
            if "Счет" in trans.get("from", "") and "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_card_from} -> Счет: {masked_card_to}")
                print(f"Сумма: {amount} {trans['operationAmount']['currency']['code']}\n")
            elif "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_card_to}")
                print(f"Сумма: {amount} {trans['operationAmount']['currency']['code']}\n")
            else:
                print(f"{correct_date} {description}")
                print(f"Транзакция: {masked_card_from} -> {masked_card_to}")
                print(f"Сумма: {amount} {trans['operationAmount']['currency']['code']}\n")
        else:
            if "Счет" in str(trans.get("from")) and "Счет" in str(trans.get("to")):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_card_from} -> Счет: {masked_card_to}")
                print(f"Сумма: {amount} {trans['currency_code']}\n")
            elif "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_card_to}")
                print(f"Сумма: {amount} {trans['currency_code']}\n")
            else:
                print(f"{correct_date} {description}")
                print(f"Транзакция: {masked_card_from} -> {masked_card_to}")
                print(f"Сумма: {amount} {trans['currency_code']}\n")


if __name__ == "__main__":
    main()
