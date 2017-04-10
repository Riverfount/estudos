"""
Programa: Soma de todos os dígitos de um inteiro
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 09 de fevereiro de 2017
"""

numero = int(input("Digite um número inteiro: "))
x = numero
soma = 0
tamanho = len(str(x))
while tamanho != 0:
    ultimoDigito = x % 10
    soma = soma + ultimoDigito
    x = x // 10
    if x != 0:
        tamanho = len(str(x))
    else:
        tamanho = 0
print(soma)