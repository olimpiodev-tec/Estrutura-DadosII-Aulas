from pessoa import Pessoa
from typing import List
import uuid

class Triagem:
    def __init__(self):
        self.atendimentos: List[Pessoa] = []
        self.prioridade_vermelho = 0
        self.prioridade_amarelo = 0

    def retirar_senha(self, pessoa: Pessoa):
        pessoa.senha = str(uuid.uuid4()).split('-')[0].upper()
        print(f"Retirando a senha de {pessoa.nome}")

        if pessoa.classificacao == "vermelho":
            self.atendimentos.insert(self.prioridade_vermelho, pessoa)

            # incrementa as duas variáveis pois
            # o amarelo vem depois do vermelho
            self.prioridade_vermelho += 1
            self.prioridade_amarelo += 1

        elif pessoa.classificacao == "amarelo":
            self.atendimentos.insert(self.prioridade_amarelo, pessoa)
            self.prioridade_amarelo += 1
        else:
            self.atendimentos.append(pessoa)

    def exibir_fila(self):
        print('\n')
        for posicao, pessoa in enumerate(self.atendimentos):
            print(f'{pessoa.nome} ({pessoa.classificacao}) - Senha: {pessoa.senha} - Posição: {posicao}')
        print('--------------------------------------\n')