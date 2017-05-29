"""
A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas 
(mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um 
descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. 
Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas 
religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.
Exemplos:

São bissextos por exemplo:
1600
1732
1888
1944
2008

Não são bissextos por exemplo:
1742
1889
1951
2011

Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""


multiplo_de = lambda base, num: num % base == 0


def bissexto(ano):

    if multiplo_de(4, ano) and not multiplo_de(100, ano) or multiplo_de(400, ano):
            return True
    else:
        return False

if __name__ == '__main__':
    assert bissexto(1600)
    assert bissexto(1732)
    assert bissexto(1888)
    assert bissexto(1944)
    assert bissexto(2008)

    assert not bissexto(1742)
    assert not bissexto(1889)
    assert not bissexto(1951)
    assert not bissexto(2011)
    assert not bissexto(2015)
