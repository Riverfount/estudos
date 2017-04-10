'''
Verifica o maior de três números sem usar lista
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 08 de março de 2017
'''

a = int(input("Entre com um número inteiro: "))
b = int(input("Entre com outro número inteiro: "))
c = int(input("Entre com um terceiro número inteiro: "))

maior = 0
menor = 0

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
if a < b and b < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c


print("Dos três números o maior é %d e o menor é %d" % (maior, menor))