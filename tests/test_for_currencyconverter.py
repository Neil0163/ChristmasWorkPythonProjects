from unittest.mock import patch, MagicMock
import pytest
from lib.CurrencyConverter import CurrencyConverter


def test_for_API():
    currencyconverter = CurrencyConverter()
    expected_api_key = 'fca_live_0Ls6TpCl1pCXmn9XpdNKHwKTs3aEwzriHLLKB2i3'
    result = currencyconverter.get_api_key()  
    assert result == expected_api_key 
    
def test_for_base_url():
    currencyconverter = CurrencyConverter()
    expected_base_url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_0Ls6TpCl1pCXmn9XpdNKHwKTs3aEwzriHLLKB2i3'
    result = currencyconverter.base_url()
    assert result == expected_base_url
    
def test_for_currencies():
    currencyconverter = CurrencyConverter()
    expected_currencies = ["USD", "GBP", "AUD", "EUR", "NZD", "JPY", "CAD"]
    result = currencyconverter.get_currencies()
    assert result == expected_currencies


def test_currency_input():
    with patch('builtins.input', return_value='USD'):
        currency_converter = CurrencyConverter()
        selected_currency = currency_converter.input()
        assert selected_currency == 'USD'
        
def test_for_invalid_currency():
    currencyconverter = CurrencyConverter()
    with patch('builtins.input', return_value="XZA"):  # Mocking user input as "XYZ" (an invalid currency)
        with pytest.raises(ValueError) as error:
            currencyconverter.input()
    assert str(error.value) == "Invalid currency. Please pick a valid currency from the list."
    




