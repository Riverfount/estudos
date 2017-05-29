"""
Desenvolva uma função que retorne um número inteiro por extenso
"""


def por_extenso(valor):
    valor_extenso = {'unidades': {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis',
                                  7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez'},

                     'except_dezenas': {11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
                                       16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'},

                     'dezenas': {2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta',
                                 7: 'setenta', 8: 'oitenta', 9: 'noventa'},

                     'centenas': {1: ['cem', 'cento'], 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos',
                                  5: 'quinhentos', 6: 'seiscentos', 7: 'setecentos', 8: 'oitocentos', 9: 'novecentos'}

                     }

    ext = []

    if 0 <= valor <= 10:
        ext.append(valor_extenso['unidades'][valor])

    elif 11 <= valor <= 19:
        ext.append(valor_extenso['except_dezenas'][valor])

    elif 20 <= valor < 100:
        ref = str(valor)
        ext.append(valor_extenso['dezenas'][int(ref[0])])
        if int(ref[-1]) != 0:
            ext.append('e')
            ext.append(valor_extenso['unidades'][int(ref[-1])])

    if valor == 100:
        ref = str(valor)
        ext.append(valor_extenso['centenas'][int(ref[0])][0 if int(ref[-1]) == 0 else 1])


    return ' '.join(ext)

if __name__ == '__main__':

    assert por_extenso(0) == 'zero'

    assert por_extenso(1) == 'um'
    assert por_extenso(2) == 'dois'
    assert por_extenso(3) == 'três'
    assert por_extenso(4) == 'quatro'
    assert por_extenso(5) == 'cinco'

    assert por_extenso(11) == 'onze'
    assert por_extenso(12) == 'doze'
    assert por_extenso(13) == 'treze'

    assert por_extenso(20) == 'vinte'
    assert por_extenso(21) == 'vinte e um'
    assert por_extenso(22) == 'vinte e dois'

    assert por_extenso(30) == 'trinta'
    assert por_extenso(31) == 'trinta e um'
    assert por_extenso(36) == 'trinta e seis'

    assert por_extenso(40) == 'quarenta'
    assert por_extenso(43) == 'quarenta e três'
    assert por_extenso(49) == 'quarenta e nove'

    assert por_extenso(50) == 'cinquenta'
    assert por_extenso(60) == 'sessenta'
    assert por_extenso(70) == 'setenta'
    assert por_extenso(80) == 'oitenta'
    assert por_extenso(99) == 'noventa e nove'

    assert por_extenso(100) == 'cem'
