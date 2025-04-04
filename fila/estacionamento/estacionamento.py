from carro import Carro
from typing import List

class Estacionamento:
    def __init__(self):
        self.vagas:List[Carro] = []

    def esta_vazio(self):
        """Verifica se o estacionamento está vazio"""
        if len(self.vagas) == 0:
            return True
        else:
            return False

    def estacionar(self, veiculo):
        """Adiciona o carro na veiculo"""
        self.vagas.append(veiculo)

    def verificar_carros_estacionados(self):
        """Retorna a qtde de carros estacionados"""
        qtde_carros = len(self.vagas)
        return qtde_carros

    def carro_saida(self):
        """Verifica o carro que vai sair da fila"""
        if self.esta_vazio():
            print('Sem carros no estacionamento')
        else:
            carro = self.vagas.pop(0)
            print('O carro que vai sair do estacionamento é')
            carro.exibir_detalhes()

    def verificar_carro_frente(self):
        """Verificar o carro que está na frente da fila"""
        if self.esta_vazio():
            print("Sem carros estacionados")
        else:
            carro_frente = self.vagas[0]
            print('O carro que está na frente da fila é')
            carro_frente.exibir_detalhes()

    def mostrar_carros_estacionados(self):
        print('Os carros que estão estacionados são')
        for carro in self.vagas:
            carro.exibir_detalhes()

    def calcular_valor(self):
        total = 0
        for carro in self.vagas:
            if carro.tipo == 'hatch':
                total += 5.00
            elif carro.tipo == 'sedan':
                total += 8.00
            elif carro.tipo == 'caminhonete':
                total += 12.00

        print(f'O valor a receber é R$ {total:.2f}')
