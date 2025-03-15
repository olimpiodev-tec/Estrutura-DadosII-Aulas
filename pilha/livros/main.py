from livro import Livro
from pilha_livros import PilhaLivros

# Inicia a pilha
meus_livros = PilhaLivros()

print(f'Está vazia: {meus_livros.esta_vazia()}')
meus_livros.tamanho()

python_fluente = Livro(titulo="Python Fluente",
                       autor="Luciano Ramalho",
                       paginas=459,
                       editora="Brasil")

meus_livros.empilhar(python_fluente)

meus_livros.tamanho()

java_programar = Livro("Java como Programar", "Paul Deitel", 934, "Brasil")

meus_livros.empilhar(java_programar)

meus_livros.tamanho()

meus_livros.topo()

meus_livros.exibir_pilha()

so = Livro(titulo='Sistemas Operacionais',
           autor='Edivaldo Serafin',
           paginas=378,
           editora='Brasil')

meus_livros.empilhar(so)

meus_livros.topo()

meus_livros.exibir_pilha()

meus_livros.topo()

meus_livros.remover_livro_pilha(java_programar.titulo)

meus_livros.exibir_pilha()




































