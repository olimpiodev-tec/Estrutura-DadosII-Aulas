from livro import Livro
from pilha_livros import PilhaLivros

codigo_limpo = Livro(titulo='Código Limpo',
                     autor='Robert C. Martin')

python_fluente = Livro('Python Fluente',
                       'Luciano Ramalho')

java_programar = Livro(autor='Paul Deitel',
                       titulo='Java como programar')

codigo_limpo.exibir_detalhes()
python_fluente.exibir_detalhes()
java_programar.exibir_detalhes()

livros = PilhaLivros()
print(livros.esta_vazia())

livros.empilhar(codigo_limpo)
livros.empilhar(python_fluente)
livros.empilhar(java_programar)

print(livros.esta_vazia())

livros.tamanho()

livros.desempilhar()
livros.desempilhar()
livros.desempilhar()

livros.tamanho()

livros.desempilhar()

livros.empilhar(codigo_limpo)
livros.empilhar(python_fluente)
livros.empilhar(java_programar)

livros.topo()

print('\n')

livros.exibir_pilha()
print('\n')

livros.mover_livro_topo(python_fluente)
print('\n')
livros.exibir_pilha()



