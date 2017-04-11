lista = [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 21, 22, 23, 24]
lista_resultante = []
lista_intermediaria = []

for i in range(len(lista)):
    if i == 0 or (lista[i] == lista[i - 1] + 1):
        lista_intermediaria.append(lista[i])
    else:
        if len(lista_intermediaria) > len(lista_resultante):
            lista_resultante = lista_intermediaria
            lista_intermediaria = []
            lista_intermediaria.append(lista[i])

if len(lista_intermediaria) > len(lista_resultante):
    lista_resultante = lista_intermediaria

print(lista_resultante)