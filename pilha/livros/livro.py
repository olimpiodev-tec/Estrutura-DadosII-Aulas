class Livro:
    def __init__(self, titulo, autor):
        self.titulo:str = titulo
        self.autor:str = autor

    def exibir_detalhes(self):
        """Mostra os detalhes do livro"""
        print(f'{self.titulo}, Autor: {self.autor}')
