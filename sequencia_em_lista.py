#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def maior_sequencia(lista):

    lista_resultante = []
    lista_intermediaria = []
    for i in range(len(lista)):
        if i == 0 or (lista[i] == lista[i - 1] + 1):
            lista_intermediaria.append(lista[i])
        else:
            if len(lista_intermediaria) > len(lista_resultante):
                lista_resultante = lista_intermediaria
                lista_intermediaria = [lista[i]]
            else:
                lista_intermediaria = [lista[i]]
    if len(lista_intermediaria) > len(lista_resultante):
        lista_resultante = lista_intermediaria
    return lista_resultante


if __name__ == '__main__':
    minha_lista = [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 21, 22, 23, 24, 35,
                   36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    print(maior_sequencia(minha_lista))
