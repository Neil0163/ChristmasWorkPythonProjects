import requests

class CurrencyConverter:
    def __init__(self):
        self.API_KEY = 'fca_live_0Ls6TpCl1pCXmn9XpdNKHwKTs3aEwzriHLLKB2i3'
        self.BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_0Ls6TpCl1pCXmn9XpdNKHwKTs3aEwzriHLLKB2i3"
        self.data = {}  # Initialize an empty dictionary to store fetched data

    def get_api_key(self):
        return self.API_KEY

    def base_url(self):
        return self.BASE_URL

    def get_currencies(self):
        return ["USD", "GBP", "AUD", "EUR", "NZD", "JPY", "CAD"]

    def convert_currency(self, base_currency):
        currencies = ",".join(self.get_currencies())
        url = f"{self.BASE_URL}&base_currency={base_currency}&currencies={currencies}"
        try:
            response = requests.get(url)
            data = response.json()
            self.data = data.get("data", {})  # Store fetched data in self.data
            return data
        except Exception as e:
            print(e)
            return None

    def formating(self):
        for ticker, value in self.data.items():
            print(f"{ticker}: {value}")

    def input(self):
        while True:
            base_currency = input("Please pick a currency: ")
            if base_currency in self.get_currencies():
                return base_currency
            else:
                raise ValueError("Invalid currency. Please pick a valid currency from the list.")

        
        
        
# Create an instance of CurrencyConverter
converter = CurrencyConverter()
# Prompt for a currency
selected_currency = converter.input()
# Fetch data by converting the selected currency
converter.convert_currency(selected_currency)
# Display the fetched data
converter.formating()


