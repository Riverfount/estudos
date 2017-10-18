def maior_na_lista(lista):

    if len(lista) == 2:
        maior = lista[0] if lista[0] > lista[1] else lista[1]
    else:
        sub_maior = maior_na_lista(lista[1:])
        maior = lista[0] if lista[0] > sub_maior else sub_maior

    return maior


if __name__ == '__main__':

    lista = [10, 2, 34, 25, 18, 44, 20, 200]

    print(f'O mairo valor na lista é: {maior_na_lista(lista)}')