from datetime import date

hoje = date.today()
ano = hoje.year

ano_carro = int(input('Qual o ano do seu veículo? '))

idade_carro = ano - ano_carro

if idade_carro > 20:
    print(f'Seu veículo não paga mais IPVA')
else:
    print(f'Seu veículo ainda paga IPVA')