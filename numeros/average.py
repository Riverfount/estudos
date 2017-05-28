"""
Programa: Calcula a média de quatro notas
Autor: Vicente Eduardo Ribeiro Marçal
Versão: 1.0
Data: 08 de fevereiro de 2017
"""
# Entra com o valor das quatro notas
Nota01 = int(input("Digite a primeira nota: "))
Nota02 = int(input("Digite a segunda nota: "))
Nota03 = int(input("Digite a terceira nota: "))
Nota04 = int(input("Digite a quarta nota: "))
Nota05 = int(input("Digite a quinta nota: "))

# Calcula a média
Media = ((Nota01 + Nota02 + Nota03 + Nota04 + Nota05) / 5)

# Imprime o resultado
print("A média aritmética é", Media)
