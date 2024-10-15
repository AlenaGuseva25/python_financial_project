import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')


def convert_to_rub(amount, currency):
    """Конвертирует сумму из заданной валюты в рубли"""
    if currency == 'RUB':
        return float(amount)

    param = {
        "from": currency,
        "to": "RUB",
        "amount": amount }
    headers = {
        "API_KEY": API_KEY }

    response =