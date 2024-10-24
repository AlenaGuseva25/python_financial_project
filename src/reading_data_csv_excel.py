import pandas as pd
import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

PATH_TO_CSV_FILE = BASE_DIR / "../data/transactions.csv"
PATH_TO_EXCEL_FILE = BASE_DIR / "../data/transactions_excel.xlsx"


def reader_file_transaction_csv(csv_path):
    """Функция принимает путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях"""
    transaction_list = []
    try:
        with open(csv_path, "r", encoding="utf-8") as transactions:
            reader = csv.DictReader(transactions, delimiter=";")
            for row in reader:
                transaction_list.append(
                    {
                        "id": str(row["id"]),
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": str(row["amount"]),
                            "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                        },
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"],
                    }
                )
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    return transaction_list


def reader_file_transaction_excel(excel_path):
    """Функция принимает путь до excel-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        transaction_df = pd.read_excel(excel_path)
        transaction_list = []
        for index, row in transaction_df.iterrows():
            transaction_list.append(
                {
                    "id": str(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": str(row["amount"]),
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"],
                        },
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
            )
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return []
    return transaction_list
