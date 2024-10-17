from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@pytest.fixture
def trans_1():
    return {"amount": 92688.46, "currency": "USD"}


@pytest.fixture
def trans_2():
    return {"amount": 92688.46, "currency": "EUR"}


@pytest.fixture
def trans_3():
    return {"amount": 0, "currency": "USD"}


@patch('requests.get')
def test_currency_conversion(mock_get, trans_1):
    mock_get.return_value.json.return_value = {"success": True, "query":
                                               {"from": "USD", "to": "RUB", "amount": "8221.37"}, "info":
                                               {"timestamp": 1724671757, "rate": 91.475458},
                                               "date": "2024-08-26", "result": 752053.58}
    assert convert_to_rub(trans_1) == 752053.58


@patch('requests.get')
def test_currency_conversion_2(mock_get, trans_2):
    mock_get.return_value.json.return_value = {"success": True, "query":
                                               {"from": "EUR", "to": "RUB", "amount": "8221.37"}, "info":
                                               {"timestamp": 1724671757, "rate": 91.475458},
                                               "date": "2024-08-26", "result": 752053.58}
    assert convert_to_rub(trans_2) == 752053.58
