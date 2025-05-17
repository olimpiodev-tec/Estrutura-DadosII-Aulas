from pessoa import Pessoa
from typing import List
import uuid

class Atendimento:
    def __init__(self):
        self.atendimentos: List[Pessoa] = []
        self.ultima_senha_prioridade = 0

    def retirar_senha(self, pessoa: Pessoa):
        # 12c84db2-0171-4a0b-a7ba-28d82e53564e
        # [12c84db2, 0171, 4a0b, a7ba, 28d82e53564e]
        senha_atendimento = str(uuid.uuid4()).split('-')[0].upper()
        pessoa.senha = senha_atendimento
        print(f'Retirando a senha do(a) {pessoa.nome}')

        if pessoa.gestante or pessoa.crianca_colo or pessoa.idade >= 60:
            # o metodo insert recebe o index e o conteudo
            self.atendimentos.insert(
                self.ultima_senha_prioridade,
                pessoa
            )
            self.ultima_senha_prioridade += 1
        else:
            self.atendimentos.append(pessoa)

    def exibir_fila(self):
        for posicao_fila, pessoa in enumerate(self.atendimentos):
            print(f'{pessoa.nome} tem a senha {pessoa.senha}'
                  f' e sua posição na fila é {posicao_fila} ')
        print('\n')










