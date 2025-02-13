"""
Crie um algoritmo que preencha
uma lista com os números de 1 até 60.
Pergunte ao usuário quantos jogos
automáticos ele quer fazer,
conforme o número de jogos crie
as listas com os numeros.
Faça o sorteo real de 6 números
Pesquisar sobre random
"""
import random
import time

print('---------MEGA SENA---------')
numeros_sorteio = [n for n in range(1, 61)]

print(f'Números da cartela {numeros_sorteio}')

numero_jogos = int(input('Quantos jogos você deseja gerar? '))

jogos_cliente = []

for jogo in range(1, numero_jogos + 1):  # para cada jogo
    lista = []
    for n in range(1, 7):  # para cada jogo preencha os números
        numero_cartela = random.choice(numeros_sorteio)
        lista.append(numero_cartela)
    jogos_cliente.append(lista)

print(f'\nOs jogos do cliente são {jogos_cliente}')

numeros_sorteados = []
print(f'\n---------Agora vamos ao sorteio---------')
for n in range(1, 7):
    print('...')
    numero_sorteado = random.choice(numeros_sorteio)
    numeros_sorteados.append(numero_sorteado)
    time.sleep(2)

print(f'Os números sorteados foram {numeros_sorteados}')

