import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
EXCHANGERATE_API_URL = "https://open.er-api.com/v6/latest"


def get_crypto_conversion_rate(from_currency, to_currency):
    params = {
        'ids': from_currency,
        'vs_currencies': to_currency
    }

    response = requests.get(COINGECKO_URL, params=params)
    data = respinse.json()
    if from_currency in data and to_currency in data[from_currency]:
        return data[from_currency][to_currency]
    else:
        raise ValueError("Invalid cryptocurrency code or API response.")



def get_fiat_conversion_rate(from_currency, to_currency):
    url = EXCHANGERATE_API_URL
    response = requests.get(url)
    data = response.json()
    if 'rates' in data and to_currency in data['rates'] and from_currency in data['rates']:
        return data['rates'][to_currency] / data['rates'][from_currency]
    else:
        raise ValueError("Invalid fiat currency code or API response. ")



def perform_conversio(amount, from_currency, to_currency):
    try:
        rate = get_crypto_conversion_rate(from_currency, to_currency)
    except ValueError:
        rate = get_fiat_conversion_rate(from_currency, to_currency)

    return amount * rate
    
















