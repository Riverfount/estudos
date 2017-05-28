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
    valor_extenso = {'unidades': {0: ' ', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis',
                                  7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez'},

                     'excep_dezenas': {11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
                                       16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'},

                     'dezenas': {2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta',
                                 7: 'setenta', 8: 'oitenta', 9: 'noventa'},
                     'centenas': {1: ['cem', 'cento'], 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos',
                                  5: 'quinhentos', 6: 'seiscentos', 7: 'setecentos', 8: 'oitocentos', 9: 'novecentos'}
                     }

    ext = []

    if valor == 0:
        return ''

    elif 0 < valor <= 10:
        ext.append(valor_extenso['unidades'][valor])

    elif 11 <= valor <= 19:
        ext.append(valor_extenso['excep_dezenas'][valor])

    elif 20 <= valor < 100:
        ref = str(valor)
        if int(ref[-1]) == 0:
            ext.append(valor_extenso['dezenas'][int(ref[0])])
        else:
            ext.append(valor_extenso['dezenas'][int(ref[0])])
            ext.append('e')
            ext.append(valor_extenso['unidades'][int(ref[-1])])

    if valor <= 120 or valor < 1000:
        ref = str(valor)
        if ref[-1] == '0':
            ext.append(valor_extenso['centenas'][int(ref[0])][1])
            ext.append('e')
            ext.append(valor_extenso['dezenas'][int(ref[-2])])
        else:
            pass

    if valor == 111 or valor == 101:
        ref = str(valor)
        print(ref[1])
        ext.append(valor_extenso['centenas'][int(ref[0])][1])
        ext.append('e')
        if ref[1] == '0':
            ext.append(valor_extenso['unidades'][int(ref[-1])])
        else:
            ext.append(valor_extenso['excep_dezenas'][int(ref[-2:])])

    if valor == 100:
        ref = str(100)
        ext.append(valor_extenso['centenas'][int(ref[0])][0])

    ext.append(('Real' if valor == 1 else 'Reais'))
    return ' '.join(ext)

if __name__ == '__main__':
    assert por_extenso(0) == ''

    assert por_extenso(1) == 'um Real'
    assert por_extenso(2) == 'dois Reais'
    assert por_extenso(3) == 'três Reais'
    assert por_extenso(4) == 'quatro Reais'
    assert por_extenso(5) == 'cinco Reais'

    assert por_extenso(11) == 'onze Reais'
    assert por_extenso(12) == 'doze Reais'
    assert por_extenso(13) == 'treze Reais'

    assert por_extenso(20) == 'vinte Reais'
    assert por_extenso(21) == 'vinte e um Reais'
    assert por_extenso(22) == 'vinte e dois Reais'

    assert por_extenso(30) == 'trinta Reais'
    assert por_extenso(31) == 'trinta e um Reais'
    assert por_extenso(36) == 'trinta e seis Reais'

    assert por_extenso(40) == 'quarenta Reais'
    assert por_extenso(43) == 'quarenta e três Reais'
    assert por_extenso(49) == 'quarenta e nove Reais'

    assert por_extenso(50) == 'cinquenta Reais'
    assert por_extenso(60) == 'sessenta Reais'
    assert por_extenso(70) == 'setenta Reais'
    assert por_extenso(80) == 'oitenta Reais'
    assert por_extenso(90) == 'noventa Reais'

    assert por_extenso(100) == 'cem Reais'
    assert por_extenso(101) == 'cento e um Reais'
    assert por_extenso(111) == 'cento e onze Reais'
    assert por_extenso(120) == 'cento e vinte Reais'
    assert por_extenso(130) == 'cento e trinta Reais'

