import csv
import json

def ler_dados_csv(nome_arquivo):
    """
    Formata a saida do arquivo lido

    {
        "C003_20230211": {
            "id_estacao": "C003",
            "data": "2023-02-11",
            "temp_max": 34.8,
            "temp_min": 12.3,
            "precipitacao_mm": 18.9,
            "umidade": 80
        },
        "D004_20230211": {
            "id_estacao": "D004",
            "data": "2023-02-11",
            "temp_max": 34.8,
            "temp_min": 12.3,
            "precipitacao_mm": 18.9,
            "umidade": 80
        }
    }
    """
    dados = {}
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            data = linha['data'].replace('-', '')
            chave = f"{linha['id_estacao']}_{data}" # D004_20230211

            dados[chave] = linha

    return dados

def busca_tabela(dados, id_estacao_data, data):
    data_sem_barras = data.replace('-', '')
    chave = f"{id_estacao_data}_{data_sem_barras}"

    registro = dados[chave]

    print(f"Registro da estacao {registro['id_estacao']} foi encontrado")
    print(f"Temperatura máxima: {registro['temp_max']}")
    print(f"Temperatura min: {registro['temp_min']}")
    print(f"Precipitação {registro['precipitacao_mm']}")

dados = ler_dados_csv('dados-estacoes-climaticas.csv')
busca_tabela(dados, 'C003', '2023-02-11')
print("\n")
busca_tabela(dados, 'D004', '2023-02-17')
print("\n")
busca_tabela(dados, 'E005', '2023-02-11')












