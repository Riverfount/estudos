

def ordena_por_selecao(lista):

    nova_lista = []
    for i in range(len(lista)):
        if i == len(lista):
            nova_lista.append(lista[i])
            return nova_lista
        else:
            if lista[i] < lista[i + 1]:
                nova_lista.append(lista[i])
            else:
                nova_lista.append(lista[i + 1])

    return nova_lista


if __name__ == '__main__':
    lista_desordenada = [14, 10, 4, 20, 17, 2, 11, 3, 6, 19, 7, 13, 5]
    print(f'Minha lista ordenada é: {ordena_por_selecao(lista_desordenada)}')
