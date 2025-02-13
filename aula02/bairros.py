bairros = [
    "Novacap", "São João", "Santa Rita", "Moreto",
    "Centro", "Jardim do Bosque", "São Luiz"
]
print(f'Bairros em qualquer ordem')
for bairro in bairros:
    print(f'O bairro é {bairro}')

bairros.sort()

print(f'Bairros em ordem alfabética')
for bairro in bairros:
    print(f'O bairro é {bairro}')