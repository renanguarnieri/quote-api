import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def consultar_cotacao(asset_id_base):
    url = f"https://rest.coinapi.io/v1/exchangerate/{asset_id_base}"

    payload = {}
    headers = {
    'Accept': 'text/plain',
    'X-CoinAPI-Key': api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

#c3c84f2d-944e-428b-9918-b42c9af37d1f