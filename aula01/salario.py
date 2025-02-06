"""
DESAFIO: crie um algoritmo que calcule o aumento
de salário do colaborador baseando se no percentual do aumento.
"""
colaborador_nome = "Moisés Francisco"
empresa = "ABC"
salario = 2456.90
percentual = 7
valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento

print(f"O colaborador {colaborador_nome}, trabalha \n"
      f"na empresa {empresa} e foi promovido com novo \n"
      f"salário de R$ {novo_salario:.2f}")