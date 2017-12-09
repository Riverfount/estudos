"""
Programa: Calcula as raízes de uma equação de segundo grau
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 08 de fevereiro de 2017
"""

import math


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


# Define a função Báskara que retorna as raízes da equação de segundo grau
def baskara(a,b,c):
    d = delta(a, b, c)
    if d < 0:
        print("Esta equação não possui raízes reais")
    elif d == 0:
        raiz = -b/(2 * a)
        print("A raiz desta equação é %5.2f" % raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("As raízes da equação são x1=%5.2f e x2=%6.2f" % (raiz1, raiz2))


print("""
      ========================================================
      ========== Resolvendo Equação do Segundo Grau ==========
      ========================================================
      """)
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
baskara(a, b, c)
