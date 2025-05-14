import csv

def ler_dados_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)

    return dados

def busca_linear(dados, id_estacao, data):
    qtde_verificacoes = 0

    for registro in dados:
        qtde_verificacoes += 1

        if registro['id_estacao'] == id_estacao and registro['data'] == data:
            print(f"Registro da estacao {registro['id_estacao']} foi encontrado")
            print(f"Temperatura máxima: {registro['temp_max']}")
            print(f"Temperatura min: {registro['temp_min']}")
            print(f"Precipitação {registro['precipitacao_mm']}")
            print(f"Qtde verificações {qtde_verificacoes}")
            break


dados = ler_dados_csv('dados-estacoes-climaticas.csv')
busca_linear(dados, 'C003', '2023-02-11')
print("\n")
busca_linear(dados, 'D004', '2023-02-17')
print("\n")
busca_linear(dados, 'E005', '2023-02-11')








