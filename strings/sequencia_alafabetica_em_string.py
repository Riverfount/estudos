#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def maior_sequencia(texto):
    texto = texto.lower()
    lista_resultante = []
    lista_intermediaria = []
    for i in range(len(texto)):
        if i == 0 or (ord(texto[i]) == (ord(texto[i - 1]) + 1)):
            lista_intermediaria.append(texto[i])
        else:
            if len(lista_intermediaria) > len(lista_resultante):
                lista_resultante = lista_intermediaria
                lista_intermediaria = [texto[i]]
            else:
                lista_intermediaria = [texto[i]]
    if len(lista_intermediaria) > len(lista_resultante):
        lista_resultante = lista_intermediaria
    return "".join(lista_resultante)


if __name__ == '__main__':
    minha_string = "abcdefgyzhtfghijklmnop"
    print(maior_sequencia(minha_string))
