class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto {self.nome}, preço {self.preco}"

def ordena_produtos(lista_produtos):
    qtde = len(lista_produtos)
    for i in range(qtde):
        min_idx = i
        for j in range(i + 1, qtde):
            if lista_produtos[j].preco < lista_produtos[min_idx].preco:
                min_idx = j

        temp = lista_produtos[i]
        lista_produtos[i] = lista_produtos[min_idx]
        lista_produtos[min_idx] = temp
    return lista_produtos

teclado = Produto(nome='Teclado Gammer', preco=459.89)
mouse = Produto(nome='Mouse', preco=34.99)
monitor = Produto(nome='Monitor', preco=299.99)

produtos = [
    teclado, mouse, monitor
]

print(f"Lista original {produtos}")
produtos_ordenados = ordena_produtos(produtos)

for produto in produtos_ordenados:
    print(produto)






















