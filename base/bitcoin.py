from forex_python.converter import CurrencyRates
import requests


def convert_brl_btc(amount):
    c = CurrencyRates()

    bitcoin_api_url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(bitcoin_api_url)
    response_json = response.json()

    usd_blr = c.get_rate('USD', 'BRL')
    btc_usd = float(response_json['data']['amount'])
    btc_brl = ((amount - 20) / (usd_blr * btc_usd))

    return round(btc_brl, 5)


if __name__ == '__main__':
    print(convert_brl_btc(1000))
