import csv
import json

def ler_vendas_csv(nome_arquivo):
    """
    Faz a leitura do csv e organiza os dados no formato abaixo:
    {
        "acessorios": {"total_itens": 450, "total_vendas": 3456.90},
        "armazenamento": {"total_itens": 390, "total_vendas": 3456.90}
    }
    """
    vendas_por_categoria = {}

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            categoria = linha['categoria']
            quantidade = int(linha['quantidade'])
            valor_unitario = float(linha['valor_unitario'])
            desconto = float(linha['desconto'])

            valor_total = quantidade * valor_unitario
            valor_total_com_desconto = valor_total - desconto

            if categoria not in vendas_por_categoria:
                vendas_por_categoria[categoria] = {
                    'total_vendas': 0.0,
                    'total_itens': 0
                }

            vendas_por_categoria[categoria]['total_vendas'] += valor_total_com_desconto
            vendas_por_categoria[categoria]['total_itens'] += quantidade

    return vendas_por_categoria

def exibir_relatorio_categoria(vendas_por_categoria, categoria_desejada):
    dados = vendas_por_categoria.get(categoria_desejada)

    total_vendas = dados['total_vendas']
    total_itens = dados['total_itens']
    valor_medio = total_vendas / total_itens

    print(f"Total vendas categoria {categoria_desejada}: R$ {total_vendas:.2f}")
    print(f"Foram vendidos {total_itens} itens")
    print(f"Valor médio por produto R$ {valor_medio:.2f}")

def menu_interativo(vendas_formatadas):

    categorias_vendas = list(vendas_formatadas.keys())

    while True:
        print("\n=== MENU DE CATEGORIAS ===")

        for i, categoria in enumerate(categorias_vendas):
            print(f"{i}. {categoria}")

        print("S ou s. Sair")

        opcao = input("\nEscolha uma categoria (número) ou (s, S) para sair: ")

        if opcao in ('S', 's'):
            print("Encerrando o programa.")
            break
        else:
            print("\n")
            opcao = int(opcao)
            categoria_escolhida = categorias_vendas[opcao]
            exibir_relatorio_categoria(vendas, categoria_escolhida)

vendas = ler_vendas_csv('dados-marketplace.csv')

menu_interativo(vendas)

# print(json.dumps(vendas, sort_keys=True, indent=4))