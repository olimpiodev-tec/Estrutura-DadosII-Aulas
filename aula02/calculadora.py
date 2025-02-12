"""
DESAFIO: escreva um algoritmo
que leia dois números e a operação
aritmética que deseja realizar,
você deve calcular para as quatro
operações soma, subtração,
multiplicação e divisão.
"""
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
operacao = int(input("Qual operação deseja realizar?\n"
                 "1->Adição, 2->Subtração, "
                 "3->Multiplicação, 4->Divisão "))

if operacao == 1:
    print(f'Resultado: {n1} + {n2} = {n1 + n2}')
elif operacao == 2:
    print(f'Resultado: {n1} - {n2} = {n1 - n2}')
elif operacao == 3:
    print(f'Resultado: {n1} * {n2} = {n1 * n2}')
elif operacao == 4:
    print(f'Resultado: {n1} / {n2} = {n1 / n2}')

