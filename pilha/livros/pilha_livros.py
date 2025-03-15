from livro import Livro
from typing import List

class PilhaLivros:
    def __init__(self):
        self.livros:List[Livro] = []

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        # return len(self.livros) == 0
        qtde_livros = len(self.livros)
        if qtde_livros == 0:
            return True
        else:
            return False

    def tamanho(self):
        """Exibir o tamanho da pilha"""
        print(f"\nA pilha tem {len(self.livros)} livros")

    def empilhar(self, livro):
        """Adiciona um livro no topo da pilha"""
        self.livros.append(livro)

    def topo(self):
        """Mostra o livro que está no topo da pilha"""
        if self.esta_vazia():
            print(f'A pilha de livros está vazia')
        else:
            livro_topo = self.livros[-1]
            print(f'O livro que esta no topo da pilha é ')
            livro_topo.exibir_detalhes()

    def exibir_pilha(self):
        """Exibe os itens da pilha de livros"""
        print('\nOs itens que estão na pilha são: \n')

        lista_invertida = reversed(self.livros)

        for livro in lista_invertida:
            livro.exibir_detalhes()

    def remover_livro_pilha(self, titulo):
        """Remove um livro da pilha"""
        for indice, livro in enumerate(self.livros):
            if livro.titulo == titulo:
                self.livros.pop(indice)
