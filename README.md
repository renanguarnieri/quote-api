# Cotação do Bitcoin em Tempo Real

Projeto em Python que consulta a cotação do Bitcoin (BTC) em Real, Dólar e Euro utilizando a API Coin e inserindo em um banco PostgreSQL os registros retornados

## Como usar

1. Clone o repositório:

    ```bash
    git clone https://github.com/renanguarnieri/quote-api.git
    cd quote-api
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script principal:

    ```bash
    python main.py
    ```

O script irá exibir a cotação do Bitcoin em Real, Dólar e Euro e inserir no banco de dados.

## Requisitos

- Python 3.8 ou superior
- requests (instalado com `requirements.txt`)
- python-dotenv (instalado com `requirements.txt`)
- pandas (instalado com `requirements.txt`)
- psycopg2 (instalado com `requirements.txt`)



