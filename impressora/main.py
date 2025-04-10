from documento import Documento
from fila_impressao import FilaImpressao
from constantes import impressao_pb, impressao_col

tcc = Documento(qtde_paginas=80, cor=impressao_pb,
                frente_verso=False, titulo='TCC')

exercicio_logica = Documento(qtde_paginas=2, cor=impressao_col,
                             frente_verso=True, titulo='Exercício Lógica')

pesquisa_uml = Documento(qtde_paginas=2, cor=impressao_col,
                         frente_verso=False, titulo='Pesquisa UML')

fila_impressao = FilaImpressao()

fila_impressao.calcular_fila_impressao()

print(f'A fila está vazia? {fila_impressao.fila_vazia()}')

fila_impressao.enviar_para_impressao(tcc)
fila_impressao.enviar_para_impressao(exercicio_logica)
fila_impressao.enviar_para_impressao(pesquisa_uml)

fila_impressao.calcular_fila_impressao()

# fila_impressao.imprimir()

# fila_impressao.mostrar_documentos_fila()

