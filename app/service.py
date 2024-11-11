import requests

BASE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_current_btc_price():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()['bpi']['USD']['rate_float']
    else:
        return f"Erro: {response.status_code}"
        