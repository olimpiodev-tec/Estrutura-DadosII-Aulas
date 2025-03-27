from aba_navegador import AbaNavegador
from typing import List
import webbrowser

class PilhaNavegador:
    def __init__(self):
        self.abas:List[AbaNavegador] = []

    def navegador_fechado(self):
        qtde_abas = len(self.abas)
        if qtde_abas == 0:
            return True
        else:
            return False
        # return len(self.abas) == 0

    def abrir_aba(self, site):
        self.abas.append(site)

    def qtde_abas(self):
        print(f'O navegador tem {len(self.abas)} abas abertas')

    def fechar_aba(self):
        if self.navegador_fechado():
            print('O navegador está fechado')
        else:
            aba = self.abas.pop()
            print(f'A aba {aba.site} foi fechada')

    def aba_ativa(self):
        if self.navegador_fechado():
            print('O navegador está fechado')
        else:
            aba_ativa = self.abas[-1]
            print('A aba que está ativa é')
            aba_ativa.exibir_detalhes()
            return aba_ativa

    def exibir_abas(self):
        print('As abas que estão abertas são:')

        for aba in reversed(self.abas):
            aba.exibir_detalhes()

    def mostrar_ultima_aba(self):
        aba_ativa = self.aba_ativa()
        caminho_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(caminho_chrome).open(aba_ativa.site)

    def mostrar_todas_abas(self):
        for aba in self.abas:
            caminho_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(caminho_chrome).open(aba.site)

