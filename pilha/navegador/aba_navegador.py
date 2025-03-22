class AbaNavegador:
    def __init__(self, site):
        self.site = site

    def exibir_detalhes(self):
        print(f'A aba do navegador está no site {self.site}')