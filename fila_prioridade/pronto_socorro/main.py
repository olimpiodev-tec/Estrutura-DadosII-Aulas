from pessoa import Pessoa
from triagem import Triagem

maria = Pessoa(nome='Maria', classificacao='verde')
joao = Pessoa(nome='João', classificacao='vermelho')
pedro = Pessoa(nome='Pedro', classificacao='amarelo')

atendimentos = Triagem()
atendimentos.retirar_senha(maria)
atendimentos.retirar_senha(joao)
atendimentos.retirar_senha(pedro)

atendimentos.exibir_fila()

barbara = Pessoa(nome='Barbara', classificacao='amarelo')
atendimentos.retirar_senha(barbara)

atendimentos.exibir_fila()

