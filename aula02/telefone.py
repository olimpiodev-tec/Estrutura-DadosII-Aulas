"""
Algoritmo que calcula a conta de telefone conforme a
quantidade de minutos utilizada

  0 até 200 minutos cobra R$ 0,20 por minuto
200 até 400 minutos cobra R$ 0,18 por minuto
mais de 400 minutos cobra R$ 0,15 por minuto
"""

minutos = int(input("Digite  quantidade de minutos"
                    " utilizada por mês: "))
valor_conta = 0

if minutos <= 200:
    valor_conta = minutos * 0.20
elif minutos > 200 and minutos <= 400: # elif 200 < minutos <= 400:
    valor_conta = minutos * 0.18
elif minutos > 400:
    valor_conta = minutos * 0.15

print(f"Sua conta mensal será de R$ {valor_conta:.2f}")