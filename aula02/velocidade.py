"""
DESAFIO: Escreva um programa que pergunte
a velocidade do carro, caso ultrapasse
80 km/h mostre uma mensagem dizendo que
o usuário foi multado.
Também mostre o valor da multa cobrando
R$ 5,00 por km acima de 80 km/h.
"""

modelo_veiculo = input('Qual o modelo do veículo? ')
radar_velocidade = int(input('Qual sua velocidade? '))

if radar_velocidade < 80:
    print(f'Siga sua viagem tranquilamento')
elif radar_velocidade == 80:
    print(f'Você está no limite da velocidade')
else:
    diferenca_velocidade = radar_velocidade - 80
    valor_multa = diferenca_velocidade * 5
    print(f'Você foi multado em R$ {valor_multa:.2f} '
          f'pois está acima da velocidade, sua velocidade '
          f'é {radar_velocidade} km/h')