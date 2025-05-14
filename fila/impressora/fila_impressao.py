from documento import Documento
from typing import List
from constantes import impressao_pb, impressao_col
from collections import deque

class FilaImpressao:
    def __init__(self):
        self.documentos: List[Documento] = []

    def fila_vazia(self):
        """Verifica se tem documentos na fila de impressão"""
        qtde_documentos = len(self.documentos)
        if qtde_documentos == 0:
            return True
        else:
            return False

    def enviar_para_impressao(self, documento):
        """Envia um documento para imprimir, vai entrar na fila de impressão"""
        self.documentos.append(documento)

    def qtde_documentos_para_imprimir(self):
        """Retorna a qtde de documentos para imprimir"""
        qtde_documentos = len(self.documentos)
        return qtde_documentos

    def imprimir(self):
        """Faz a impressão do documento"""
        if self.fila_vazia():
            print('Impressora não tem documentos para imprimir')
        else:
            total = FilaImpressao.calcular_valor_impressao_documento(self.documentos[0])

            if total == 0:
                print(f'O documento {self.documentos[0].titulo} não será impresso')
                self.documentos.pop(0)
            else:
                documento_impresso = self.documentos.pop(0)
                print('O documento que está sendo impresso é')
                documento_impresso.exibir_detalhes()

    def mostrar_documentos_fila(self):
        print('---Documentos da fila de impressão---')
        for documento in self.documentos:
            documento.exibir_detalhes()

    def calcular_fila_impressao(self):
        print(f'\nCalculando valores da impressora')

        total_fila = 0
        for documento in self.documentos:
            total_fila += FilaImpressao.calcular_valor_impressao_documento(documento)

        print(f'O total á receber pela fila de impressão é R$ {total_fila:.2f}')

    @staticmethod
    def calcular_valor_impressao_documento(documento):
        total_documento = 0

        if documento.frente_verso:
            """PB 0,25 e Colorido 0,45"""
            if documento.cor == impressao_pb:
                total_documento = documento.qtde_paginas * 0.25
            elif documento.cor == impressao_col:
                total_documento = documento.qtde_paginas * 0.45
        else:
            """PB 0,35 e Colorido 0,55"""
            if documento.cor == impressao_pb:
                total_documento = documento.qtde_paginas * 0.35
            elif documento.cor == impressao_col:
                total_documento = documento.qtde_paginas * 0.55

        if total_documento > 10:
            print(f'Documento {documento.titulo} não será impresso pois custa R$ {total_documento:.2f}')
            return 0
        else:
            print(f'O valor da impressão é R$ {total_documento:.2f}')
            return total_documento
