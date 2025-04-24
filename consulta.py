import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")



def consultar_cotacao(asset_id_base,quote):
    url = f"https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{quote}"

    payload = {}
    headers = {
    'Accept': 'text/plain',
    'X-CoinAPI-Key': api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

quotes = ['USD', 'BRL', 'EUR']

def filtrar_quotes(origem, moeda):
    datas = []
    for m in moeda:
        result = consultar_cotacao(origem,m)
        datas.append(result)
    return datas
    

def criar_df():
    cotacoes = pd.DataFrame(filtrar_quotes('BTC',quotes))
    print(cotacoes)
