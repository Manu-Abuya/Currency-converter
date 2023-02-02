import requests

# API endpoint for exchange rates
EXCHANGE_RATE_API = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rate(from_currency, to_currency):
    # Get the exchange rates data from the API
    response = requests.get(EXCHANGE_RATE_API)
    data = response.json()
    
    # Check if the from_currency is present in the exchange rates data
    if from_currency in data["rates"]:
        # Check if the to_currency is present in the exchange rates data
        if to_currency in data["rates"]:
            # Calculate the exchange rate
            exchange_rate = data["rates"][to_currency] / data["rates"][from_currency]
            return exchange_rate
        else:
            return "Error: to_currency not found in exchange rates data."
    else: 
        return "Error: from_currency not found in exchange rates data."