class Livro:
    def __init__(self, titulo, autor, paginas, editora):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editora = editora

    def exibir_detalhes(self):
        """Mostra os detalhes do livro"""
        print(f'{self.titulo} Autor: {self.autor}, '
              f'Qtde páginas {self.paginas}, '
              f'Editora {self.editora}')
