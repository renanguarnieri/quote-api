import requests
from dotenv import load_dotenv
import os
import pandas as pd
import psycopg2

load_dotenv()
api_key = os.getenv("API_KEY")

# Conectar ao PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    database=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    port=os.getenv('PG_PORT')  # opcional, 5432 é padrão
)

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
    

def filtrar_quotes(origem, moedas):
    return [consultar_cotacao(origem, m) for m in moedas]

def inserir_cotacoes_no_banco(dados):
    cur = conn.cursor()
    for item in dados:
        cur.execute("""
            INSERT INTO current_all_rates (asset_base, asset_cid_quote, rate, time)
            VALUES (%s, %s, %s, %s)
        """, (
            item['asset_id_base'],
            item['asset_id_quote'],
            item['rate'],
            item['time']
        ))
    conn.commit()
    cur.close()
    print("Dados inseridos com sucesso.")

def main():
    cotacoes = filtrar_quotes('BTC', quotes)
    inserir_cotacoes_no_banco(cotacoes)