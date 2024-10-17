import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def convert_to_rub(transaction_convert) -> float:
    """Принимает значение в долларах или евро, обращается к внешнему API и возвращает конвертацию в рубли"""
    if not isinstance(transaction_convert, dict):
        raise ValueError("Входными данными должен быть словарь")

    from_curr = transaction_convert.get("operationAmount", {}).get("currency", {}).get("code")
    amount = transaction_convert.get("operationAmount", {}).get("amount")

    if from_curr is None or amount is None:
        raise ValueError("Неверные данные транзакции")

    headers = {"apikey": api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_curr}&amount={amount}"

    if from_curr == "RUB":
        return amount
    elif from_curr != "RUB":
        result = requests.get(url, headers=headers)
        new_amount = result.json()
        return new_amount["result"]


if __name__ == "__main__":
    print(
        convert_to_rub(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
    )
