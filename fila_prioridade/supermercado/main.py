from pessoa import Pessoa
from mercado import Supermercado

joao = Pessoa(nome='João', idade=45, qtde_itens=20)
pedro = Pessoa(nome='Pedro', idade=68, qtde_itens=40)
maria = Pessoa(nome='Maria', idade=18, qtde_itens=2)

covabra = Supermercado()
covabra.retirar_senha(joao)
covabra.retirar_senha(pedro)
covabra.retirar_senha(maria)

covabra.exibir_fila()

barbara = Pessoa(nome='Barbara', idade=61, qtde_itens=55)
covabra.retirar_senha(barbara)

covabra.exibir_fila()