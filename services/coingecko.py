import requests

def get_prices(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()
