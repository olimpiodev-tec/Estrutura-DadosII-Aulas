class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Nome: {self.nome}, idade: {self.idade}"


def ordena_idade(lista_pessoas):
    qtde_pessoas = len(lista_pessoas)
    for i in range(qtde_pessoas):
        min_idx = i
        for j in range(i+1, qtde_pessoas):
            if lista_pessoas[j].idade < lista_pessoas[min_idx].idade:
                min_idx = j

        temp = lista_pessoas[i]
        lista_pessoas[i] = lista_pessoas[min_idx]
        lista_pessoas[min_idx] = temp
    return lista_pessoas

jonas = Pessoa(nome='Jonas', idade=45)
barbara = Pessoa(nome='Barbara', idade=36)
claudia = Pessoa(nome='Claudia', idade=12)
rafael = Pessoa(nome='Rafael', idade=8)
marcos = Pessoa(nome='Marcos', idade=39)

pessoas = [
    jonas, barbara, claudia, rafael, marcos
]

print(f"Pessoas: {pessoas}")
pessoas_idade = ordena_idade(pessoas)
print(f"Pessoas ordenadas pela idade: {pessoas_idade}")













