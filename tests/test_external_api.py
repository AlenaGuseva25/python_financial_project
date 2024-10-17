from unittest.mock import patch
import pytest


from src.external_api import convert_to_rub


def test_convert_to_rub_success_usd():
    transaction = {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 7500.0}

        result = convert_to_rub(transaction)
        assert result == 7500.0
        mock_get.assert_called_once()


def test_convert_to_rub_success_euro():
    transaction = {"operationAmount": {"currency": {"code": "EUR"}, "amount": "100"}}

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 8500.0}

        result = convert_to_rub(transaction)
        assert result == 8500.0
        mock_get.assert_called_once()


def test_convert_to_rub_rub_success():
    transaction = {"operationAmount": {"currency": {"code": "RUB"}, "amount": "100"}}


def test_convert_to_rub_invalid_input():
    with pytest.raises(ValueError, match="Входными данными должен быть словарь"):
        convert_to_rub("invalid input")

    with pytest.raises(ValueError, match="Неверные данные транзакции"):
        convert_to_rub({"operationAmount": {}})

    with pytest.raises(ValueError, match="Неверные данные транзакции"):
        convert_to_rub({"operationAmount": {"currency": {}}})


def test_convert_to_rub_no_currency_or_amount():
    transaction = {"operationAmount": {"currency": {"code": None}, "amount": None}}
