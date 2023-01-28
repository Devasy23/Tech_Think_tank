import requests
import json

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = json.loads(response.text)
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

# Function to make a money transfer
def make_transfer(amount, from_currency, to_currency, recipient_info):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    # Code to send the converted amount to the recipient
    # ...
    return 'Transfer complete'

# Example usage
transfer_amount = 100
sender_currency = 'USD'
recipient_currency = 'EUR'
recipient_info = {'name': 'John Doe', 'account_number': '123456'}
print(make_transfer(transfer_amount, sender_currency, recipient_currency, recipient_info))
# Output: Transfer complete