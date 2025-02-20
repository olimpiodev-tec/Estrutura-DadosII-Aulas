"""
Crie um código que simule uma calculadora
para números decimais para as quatro
operações matemáticas.
Os números precisam ser inseridos
pelo usuário. Use funções
"""
def calcular(n1, n2, operacao):
    if operacao == 1:
        print(f'Resultado: {n1} + {n2} = {n1 + n2}')
    elif operacao == 2:
        print(f'Resultado: {n1} - {n2} = {n1 - n2}')
    elif operacao == 3:
        print(f'Resultado: {n1} * {n2} = {n1 * n2}')
    elif operacao == 4:
        print(f'Resultado: {n1} / {n2} = {n1 / n2}')

numero1 = float(input("Digite o primeiro número "))
numero2 = float(input("Digite o segundo número "))
op = int(input("Qual operação deseja realizar?\n"
                 "1->Adição, 2->Subtração, "
                 "3->Multiplicação, 4->Divisão "))

calcular(numero1, numero2, op)

