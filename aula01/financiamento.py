"""
DESAFIO: crie um algoritmo que calcule o valor
da parcela do financiamento de um veículo
Também pergunte a data de pagamento
"""
print('Seja bem vindo ao simulador de financiamentos')

cliente = input('Qual seu nome? ')
veiculo = input('Qual o veículo? ')
valor = float(input(f'Qual o valor do {veiculo}? '))
qtde_parcelas = int(input('Em quantas parcelas deseja pagar? '))
valor_parcela = valor / qtde_parcelas

print(f'Prezado {cliente}, o veículo {veiculo} \n'
      f'custa R$ {valor:.2f} será pago em {qtde_parcelas} \n'
      f'parcelas com valor de R$ {valor_parcela:.2f}')

