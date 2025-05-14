class Documento:
    def __init__(self, qtde_paginas, cor, frente_verso, titulo):
        self.qtde_paginas = qtde_paginas
        self.cor = cor
        self.frente_verso = frente_verso
        self.titulo = titulo

    def exibir_detalhes(self):
        print(f'Documento {self.titulo} tem {self.qtde_paginas} páginas na cor {self.cor}')
        print(f'Documento será impresso frente e verso '
              f'{"Sim" if self.frente_verso else "Não"} \n')
