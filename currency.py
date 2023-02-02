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
    

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    # Check if the exchange rate is valid
    if type(exchange_rate) == float:
        # Calculate the converted amount
        converted_amount = exchange_rate * amount
        return converted_amount
    else:
        return exchange_rate
    

# Main function to run the currency converter
def run_currency_converter():
    
    # Get the amount to be converted
    amount = float(input("Enter the amount to be converted: "))
    
    # Get the currency to convert from
    from_currency = input("Enter the currency to convert from (e.g. USD): ").upper()
  
    # Get the currency to convert to
    to_currency = input("Enter the currency to convert to (e.g. EUR): ").upper()
   
    # Convert the currency
    converted_amount = convert_currency(amount, from_currency, to_currency)
   
    # Print the result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    
    
# Run the currency converter
run_currency_converter()