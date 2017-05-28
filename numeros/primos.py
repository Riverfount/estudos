"""
Programa: Verifica se o número informado é primo
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 09 de fevereiro de 2017
"""

numero = int(input("Digite um número inteiro: "))
i = numero
numPrimo = True
while numPrimo and i > 2:
    i = i - 1
    if (numero % i) == 0:
        numPrimo = False
if numPrimo:
    print("primo")
else:
    print("não primo")