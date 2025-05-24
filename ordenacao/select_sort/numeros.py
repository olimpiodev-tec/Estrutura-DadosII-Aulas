def ordena_menor_para_maior(lista):

    qtde_itens = len(lista)

    # Iteração passando por todos os elementos da lista
    for i in range(qtde_itens):

        # Armazena o index atual
        min_idx = i

        # Iteração interna, passa por todos os elementos
        # Verificando quem é o maior
        for j in range(i+1, qtde_itens):

            # Verifica quem é o menor comparando
            if lista[j] < lista[min_idx]:
                min_idx = j

        temp = lista[i] # Armazena temporariamente
        lista[i] = lista[min_idx] # Faz a substituição dos valores swap
        lista[min_idx] = temp # Volta o valor temp na lista

    return lista

lista = [45, 2, 890, 34, 1, 3, 56]
print(f"Lista Original: {lista}")

lista_ordenada = ordena_menor_para_maior(lista.copy())
print(f"Lista Ordenada: {ordena_menor_para_maior(lista)}")




