import json
from unittest.mock import patch, mock_open
from src.utils import financial_transactions


def test_financial_transactions_file_not_found():
    with patch("os.path.exists", return_value=False):
        assert financial_transactions("Несуществующий файл.json") == []


def test_financial_transactions_invalid_json():
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data="{invalid json}")):
            with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
                assert financial_transactions("Недопустимый файл.json") == []


def test_financial_transaction_not_a_list():
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            assert financial_transactions("Не является списком.json") == []


def test_financial_transaction_valid_list():
    with patch("os.path.exists", return_value=True):
        expected_data = [
            {
                "id": 619287771,
                "state": "EXECUTED",
                "date": "2019-08-19T16:30:41.967497",
                "operationAmount": {"amount": "81150.87", "currency": {"name": "USD", "code": "USD"}},
            }
        ]

        with patch("builtins.open", mock_open(read_data=json.dumps(expected_data))):
            assert financial_transactions("Действительный файл.json") == expected_data
