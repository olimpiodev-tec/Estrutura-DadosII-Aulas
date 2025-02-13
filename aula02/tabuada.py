"""
Peça ao usuário um número e
imprima a tabuada do 1 até 10
desse número
"""
numero = int(input('Qual tabuada deseja visualizar? '))

"""
Função range(start, stop, step)
Sendo que o stop precisa ser + 1
"""
for n in range(1, 11):
    print(f'{n} x {numero} = {n * numero}')