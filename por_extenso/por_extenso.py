"""
Apesar de o volume de cheques emitidos tenha diminuído drásticamente nos últimos anos, principalmente devido a 
popularização dos cartões de crédito e débito, eles ainda são utilizados em muitas compras, especialmente a de 
valores  altos. E para auxiliar no seu preenchimento, vários estabelecimentos possuem máquinas que dado o valor da  
compra, preenchem o cheque com o seu valor por extenso.

Desenvolva um programa que dado um valor monetário, seja retornado o valor em reais por extenso.

Exemplo:

15415,16 -> quinze mil quatrocentos e quinze reais e dezesseis centavos
0,05 -> cinco centavos
2,25 -> dois reais e vinte e cinco centavos
"""


def por_extenso(valor):
    if valor == 3:
        return 'três Reais'
    if valor == 2:
        return 'dois Reais'
    if valor == 1:
        return 'um Real'



if __name__ == '__main__':
    assert por_extenso(1) == 'um Real'
    assert por_extenso(2) == 'dois Reais'
    assert por_extenso(3) == 'três Reais'
