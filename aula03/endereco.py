"""
Crie um algoritmo que busque o endereço
da pessoa conforme o cep. Use funções
e dicionários.
"""
import requests
import json

def buscar(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    req = requests.get(url)
    response = req.json()
    print(f'{json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False)}')

cep = input('Qual o cep que deseja consultar o endereço? ')
buscar(cep)






