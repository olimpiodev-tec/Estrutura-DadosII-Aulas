from pessoa import Pessoa
from typing import List
import uuid

class Supermercado:
    def __init__(self):
        self.atendimentos: List[Pessoa] = []
        self.fila_preferencial = 0
        self.fila_rapida = 0

    def retirar_senha(self, pessoa: Pessoa):
        senha_atendimento = str(uuid.uuid4()).split('-')[0].upper()
        senha_menor = senha_atendimento[0:3]
        pessoa.senha = senha_menor

        print(f"Retirando a senha de {pessoa.nome}")

        if pessoa.idade >= 60:
            self.atendimentos.insert(self.fila_preferencial, pessoa)
            self.fila_preferencial += 1
            self.fila_rapida += 1
        elif pessoa.qtde_itens <= 10:
            self.atendimentos.insert(self.fila_rapida, pessoa)
            self.fila_rapida += 1
        else:
            self.atendimentos.append(pessoa)

    def exibir_fila(self):
        print('\n')
        for posicao, pessoa in enumerate(self.atendimentos):
            print(f'{pessoa.nome} - {pessoa.qtde_itens} itens - Senha: {pessoa.senha} - Posição: {posicao}')
        print('--------------------------------------\n')