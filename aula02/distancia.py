"""
DESAFIO: crie um algoritmo que
pergunte a distância que um
passageiro deseja percorrer
em km. Calcule o preço da
passagem cobrando R$ 0,50
por km para viagens até 200 km,
e R$ 0,45 para viagens mais longas
"""
cliente = input('Qual seu nome? ')
distancia = int(input(f'{cliente} quantos kilometros '
                      f'você vai percorrer até destino? '))

print(f'{cliente}, sua viagem vai custar '
      f'R$ {distancia * 0.50 if distancia <= 200 else distancia * 0.45}')

# if distancia <= 200:
#     print(f'{cliente} sua viagem vai custar '
#           f'R$ {distancia * 0.50:.2f}')
# else:
#     print(f'{cliente} sua viagem vai custar '
#           f'R$ {distancia * 0.45:.2f}')