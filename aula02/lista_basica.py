numeros = [12, 78, 459, 901]

print(f'{numeros}')
print(f'O segundo número é {numeros[1]}')
print(f'O último número é {numeros[-1]}')

# Adicionando elementos na lista
numeros.append(289)
print(f'Append na lista {numeros}')

# Remover elementos da lista
numeros.remove(78)
print(f'Remover {numeros}')

# Obtendo o índice do elemento
print(f'O índice do número 459 é {numeros.index(459)}')