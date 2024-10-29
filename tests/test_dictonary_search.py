import unittest
from src.dictonary_search import search_transactions, count_transactions


class TestFinancialFunctions(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {"description": "Перевод со счета на счет", "amount": 100},
            {"description": "Оплата коммунальных услуг", "amount": 50},
            {"description": "Покупка в магазине", "amount": 30},
            {"description": "Перевод на карту", "amount": 150},
            {"description": "Оплата за интернет", "amount": 20},
        ]

    def test_search_transactions(self):
        result = search_transactions(self.transactions, "Перевод")
        self.assertEqual(len(result), 2)

        result = search_transactions(self.transactions, "Оплата")
        self.assertEqual(len(result), 2)

        result = search_transactions(self.transactions, "Неизвестная категория")
        self.assertEqual(len(result), 0)

    def test_count_transactions(self):
        user_categories = ["Перевод", "Оплата коммунальных услуг"]
        result = count_transactions(self.transactions, user_categories)

        self.assertEqual(result["Перевод"], 2)
        self.assertEqual(result["Оплата коммунальных услуг"], 1)

        self.assertEqual(result.get("Неизвестная категория", 0), 0)

    def test_count_transactions_empty(self):
        user_categories = []
        result = count_transactions(self.transactions, user_categories)
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
