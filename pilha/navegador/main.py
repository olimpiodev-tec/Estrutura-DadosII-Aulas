from aba_navegador import AbaNavegador
from pilha_navegador import PilhaNavegador

ifsp = AbaNavegador(site="cpv.ifsp.edu.br")
google = AbaNavegador(site="google.com")
github = AbaNavegador(site="github.com")

abas = PilhaNavegador()
abas.qtde_abas()

abas.abrir_aba(ifsp)
abas.abrir_aba(google)
abas.abrir_aba(github)

abas.qtde_abas()

abas.fechar_aba()

abas.aba_ativa()

abas.mostrar_ultima_aba()

abas.mostrar_todas_abas()

