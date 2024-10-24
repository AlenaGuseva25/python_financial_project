import unittest
from unittest.mock import mock_open, patch
import pandas as pd
from src.reading_data_csv_excel import reader_file_transaction_csv, reader_file_transaction_excel


class TestTransactionReaders(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data="id;state;date;amount;currency_name;currency_code;from;to;description"
                     "\n1;completed;2023-01-01;100;""USD;840;account1;account2;Transaction 1")
    def test_reader_file_transaction_csv(self, mock_file):
        csv_path = "dummy_path.csv"
        expected_result = [{
            "id": "1",
            "state": "completed",
            "date": "2023-01-01",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "840"},
            },
            "description": "Transaction 1",
            "from": "account1",
            "to": "account2",
        }]

        result = reader_file_transaction_csv(csv_path)
        self.assertEqual(result, expected_result)

    @patch("pandas.read_excel")
    def test_reader_file_transaction_excel(self, mock_read_excel):
        excel_path = "dummy_path.xlsx"
        mock_data = pd.DataFrame({
            "id": [1],
            "state": ["completed"],
            "date": ["2023-01-01"],
            "amount": [100],
            "currency_name": ["USD"],
            "currency_code": ["840"],
            "from": ["account1"],
            "to": ["account2"],
            "description": ["Transaction 1"]
        })
        mock_read_excel.return_value = mock_data

        expected_result = [{
            "id": "1",
            "state": "completed",
            "date": "2023-01-01",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "840"},
            },
            "description": "Transaction 1",
            "from": "account1",
            "to": "account2",
        }]

        result = reader_file_transaction_excel(excel_path)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
