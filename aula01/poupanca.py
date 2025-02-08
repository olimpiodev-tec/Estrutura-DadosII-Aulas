"""
DESAFIO: Você deseja fazer uma poupança
mensal com 30% do seu salário atual.
Seu objetivo é guardar dinheiro por 2 anos.
O banco está aplicando 5% por mês de
rendimento no valor.
Calcule o valor guardado ao final dos
2 anos
"""
print('Seja bem vindo ao simulador de poupança')

cliente = input('Qual seu nome? ')
salario = float(input('Qual seu salário? '))
meses = int(input('Qual o período (meses) que deseja poupar? '))

rendimento_total = meses * (5 / 100)
salario30 = salario * (30 / 100)
total30_meses = salario30 * meses
total = total30_meses + (total30_meses * rendimento_total)

print(f'Prezado {cliente} o valor de 30% R$ {salario30:.2f} \n'
      f'guardado por {meses} meses vai render ao final \n'
      f'R$ {total:.2f}')
