import random


def qsorty(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return qsorty(menores) + [pivo] + qsorty(maiores)


if __name__ == '__main__':
    lista_desrodenada = [random.randrange(300) for i in range(20)]

    print(f'A lista desordenada é: {lista_desrodenada}')
    print()
    print(f'A lista ordenada é: {qsorty(lista_desrodenada)}')