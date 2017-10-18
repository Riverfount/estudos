def menor_elemento(lista):
    menor_elemento = lista[0]
    menor_indice = 0

    for i, elemento in enumerate(lista):
        if elemento < menor_elemento:
            menor_elemento = elemento
            menor_indice = i

    return menor_indice


def ordena_por_selecao(lista):

    nova_lista = []
    for i in range(len(lista)):
        menor = menor_elemento(lista)
        nova_lista.append(lista.pop(menor))

    return nova_lista


if __name__ == '__main__':
    lista_desordenada = [14, 10, 4, 20, 17, 2, 11, 3, 6, 19, 7, 13, 5]
    print(f'Minha lista ordenada é: {ordena_por_selecao(lista_desordenada)}')
