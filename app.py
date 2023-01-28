import requests
import json

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = json.loads(response.text)
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate
    print(converted_amount)
    return converted_amount

# Function to make a money transfer
def make_transfer(amount, from_currency, to_currency, recipient_info):
    converted_amount = convert_currency(amount, from_currency, to_currency)
    # Code to send the converted amount to the recipient
    # ...
    print(converted_amount)
    name = recipient_info['name']
    account_number = recipient_info['account_number']
    return f'Transfer complete from {name}, account {account_number}', converted_amount

# Example usage
transfer_amount = 100
sender_currency = 'USD'
recipient_currency = 'EUR'
recipient_info = {'name': 'John Doe', 'account_number': '123456'}
print(make_transfer(transfer_amount, sender_currency, recipient_currency, recipient_info))
# Output: Transfer complete