import re
import collections

from src.reading_data_csv_excel import reader_file_transaction_csv, reader_file_transaction_excel
from src.utils import financial_transactions


json_file = financial_transactions("..//data/operations.json")
csv_file = reader_file_transaction_csv("..//data/transactions.csv")
excel_file = reader_file_transaction_excel("..//data/transactions_excel.xlsx")


def search_transactions(transactions, search_string):
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    results = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    for transaction in transactions:
        desc = transaction.get("description", "")
        if isinstance(desc, str) and re.search(pattern, desc):
            results.append(transaction)

    return results


def count_transactions(transactions: list[dict], user_categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
        а значения — это количество операций в каждой категории"""
    count = collections.Counter()

    for transaction in transactions:
        descriptions = transaction.get("description", "").lower()

        for category in user_categories:
            if category.lower() in descriptions:
                count[category] += 1
    return dict(count)
