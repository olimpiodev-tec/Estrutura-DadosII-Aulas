from pessoa import Pessoa
from atendimento import Atendimento

joao = Pessoa(nome='João', idade=34)
pedro = Pessoa(nome='Pedro', idade=26)
barbara = Pessoa(nome='Barbara', idade=60)

toten = Atendimento()

toten.retirar_senha(joao)
toten.retirar_senha(pedro)
toten.retirar_senha(barbara)

toten.exibir_fila()

maria = Pessoa(nome='Maria', idade=35, gestante=True)
toten.retirar_senha(maria)

toten.exibir_fila()

jose = Pessoa(nome='Jose', idade=40, crianca_colo=True)
toten.retirar_senha(jose)

toten.exibir_fila()












