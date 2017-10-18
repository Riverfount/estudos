def count_list(lista):

    if lista == []:
        total_elementos = 0
    else:
        total_elementos = 1 + count_list(lista[1:])

    return total_elementos


if __name__ == '__main__':

    lista_ref = [x for x in range(300)]

    print(f'O total de elementos de minha lista é de: {count_list(lista_ref)}')