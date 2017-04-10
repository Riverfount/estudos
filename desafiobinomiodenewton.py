"""
Programa: Calcula o binômio de Newton
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 09 de fevereiro de 2017
"""


def fatorial(numero):
        fat = 1
        while numero != 0:
            fat = fat * numero
            numero -= 1
        return fat

n = int(input("Entre com o valor de n: "))
k = int(input("Entre com o valor de k: "))

if k <= n:
    binomio = int(fatorial(n) / (fatorial(k) * fatorial(n - k)))
    print("O resultado do Binômio de Newton para %d e %d é: %d"
          % (n, k, binomio))
else:
    print("Não há como calcular o Binômio de Newton pois %d é maior que %d"
          % (k, n))
