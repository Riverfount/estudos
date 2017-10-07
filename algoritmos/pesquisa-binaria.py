

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        elif chute < item:
            baixo = meio + 1
    return None


if __name__ == '__main__':
    minha_lista = [x for x in range(101)]
    print(f'{pesquisa_binaria(minha_lista, 30)}')
    print(f'{pesquisa_binaria(minha_lista, 15)}')
    print(f'{pesquisa_binaria(minha_lista, 100)}')
    print(f'{pesquisa_binaria(minha_lista, 300)}')
    print(f'{pesquisa_binaria(minha_lista, 1)}')
    print(f'{pesquisa_binaria(minha_lista, 10)}')
    print(f'{pesquisa_binaria(minha_lista, 50)}')
    print(f'{pesquisa_binaria(minha_lista, 150)}')
