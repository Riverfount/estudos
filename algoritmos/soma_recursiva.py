def soma_recursiva(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])


if __name__ == '__main__':
    lista = [2, 3, 4, 5, 20]
    print(f'A soma dos elementos da lista é: {soma_recursiva(lista)} ')
