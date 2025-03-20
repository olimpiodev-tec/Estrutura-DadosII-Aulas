from livro import Livro
from typing import List

class PilhaLivros:
    def __init__(self):
        self.livros:List[Livro] = []

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        qtde_livros = len(self.livros)

        if qtde_livros == 0:
            return True
        else:
            return False
        # return len(self.livros) == 0

    def empilhar(self, livro):
        """Adiciona um livro na pilha"""
        self.livros.append(livro)

    def tamanho(self):
        """Retorna o tamanho da pilha"""
        print(f'A pilha tem {len(self.livros)} livros')

    def desempilhar(self):
        """Remove um livro da pilha"""
        if self.esta_vazia():
            print('A pilha está vazia')
        else:
            livro = self.livros.pop()
            print(f'O livro {livro.titulo} foi retirado da pilha')
            return livro

    def topo(self):
        """Verificar qual item está no topo da pilha"""
        if self.esta_vazia():
            print('A pilha está vazia')
        else:
            livro_topo = self.livros[-1]
            print('O livro que está no topo da pilha é')
            livro_topo.exibir_detalhes()

    def exibir_pilha(self):
        """Exibe os itens da pilha"""
        print('Os livros que estão na pilha são:')

        for livro in reversed(self.livros):
            livro.exibir_detalhes()

    def mover_livro_topo(self, livro_mover):
        """Move um livro específico para topo da pilha"""
        pilha_aux = []
        livro_procurado = None

        while not self.esta_vazia():
            livro = self.desempilhar()
            if livro.titulo == livro_mover.titulo:
                livro_procurado = livro
                break

            pilha_aux.append(livro)

        for livro_desempilhado in pilha_aux:
            self.empilhar(livro_desempilhado)

        self.empilhar(livro_procurado)















