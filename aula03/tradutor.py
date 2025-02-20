"""
Crie um algoritmo que gere um tradutor
para dois idiomas, use dicionários e funções.
O usuário vai pesquisar por uma palavra
e o idioma, você deve retornar a tradução.
Caso não encontre retorne "Tradução não disponível"
"""
dicionario = {
    "en": { # pt to en
        "arquivo": "file",
        "iniciar": "boot",
        "pasta": "folder",
        "senha": "password"
    },
    "pt": { # en to pt
        "file": "arquivo",
        "boot": "iniciar",
        "folder": "pasta",
        "password": "senha"
    }
}

def traduzir(idioma, palavra):
    if idioma != "pt" and idioma != "en":
        return "Idioma não disponível"

    palavras_idioma = dicionario[idioma]
    for chave, valor in palavras_idioma.items():
        if chave == palavra:
            return (f'A palavra {palavra.upper()} traduzida '
                    f'para idioma {idioma.upper()} é {valor.upper()}')

    return f'Tradução não disponível'

palavra = input("Qual a palavra que deseja traduzir? ")
idioma = input("Qual o idioma [pt] ou [en]? ")

palavra_traduzida = traduzir(idioma, palavra)
print(palavra_traduzida)