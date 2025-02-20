import json

aluno = {
    "nome": "Moises",
    "idade": 42,
    "cursos": [
        "Análise e Desenvolvimento de Sistemas",
        "Desenvolvimento para Dispositivos Móveis"
    ]
}

print(f"O aluno {aluno['nome']} é muito empenhado nos estudos")

# print(f"A idade do aluno é {aluno['idade_aluno']}")
print(f"A idade do aluno é {aluno.get('idade_aluno')}") # Não gera o erro

# Não gera o erro e define o valor padrão
print(f"A idade do aluno é {aluno.get('idade_aluno', 18)}")

# Adicionando propriedade no dicionário
aluno['nota1'] = 6.7
print(json.dumps(aluno, sort_keys=True, indent=4))

# Removendo uma chave
aluno.pop('nota1')
print(json.dumps(aluno, sort_keys=True, indent=4))

# Limpando o dicionário
# aluno.clear()
# print(json.dumps(aluno, sort_keys=True, indent=4))

# Iterando sobre o dicionário
# Mostra somente as chaves do dicionário
for chave in aluno:
    print(chave)

# Mostra os valores do dicionário
for valor in aluno.values():
    print(valor)

# Mostra as chaves e os valores
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')






