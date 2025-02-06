print('Olá vamos realizar a conversão do seu dinheiro')

valor_reais = input('Qual a quantia em reais que deseja converter?')
valor_dolar = input('Qual o valor do dólar?')

valor_convertido = float(valor_reais) / float(valor_dolar)

print(f'O valor R$ {valor_reais} convertido em U$ {valor_convertido}')