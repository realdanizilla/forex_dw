import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():# URL endpoint for the Coinbase API to get the current price of Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"


    # Requisição GET
    response = requests.get(url)
    #print(response.json())

    data = response.json()

    # Extrair os dados que eu quero
    preco = float(data['data']['amount'])
    ativo = data['data']['base']
    moeda = data['data']['currency']
    data_coleta = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    #print(preco)
    #print(ativo)
    #print(moeda)
    #print(data_coleta)

    dataframe = pd.DataFrame({
        'ativo': [ativo],
        'moeda': [moeda],
        'preco': [preco],
        'data_coleta': [data_coleta]
    })
    return dataframe
    #print(dataframe)

 