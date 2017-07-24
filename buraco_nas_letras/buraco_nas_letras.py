def conta_buracos_no_texto(texto):
    """
    Se você pensar em um papel como um plano e uma letra como uma marcação neste plano, então estas letras dividem o
    plano em regiões. Por exemplo, as letras A, D e O dividem o plano em 2 pois possuem um espaço confinado em seu
    desenho, ou um “buraco”. Outras letras como B possuem 2 buracos e letras como C e E não possuem buracos.

    Deste modo podemos considerar que o número de buracos em um texto é igual a soma dos buracos nas palavras dele.

    A sua tarefa é, dado um texto qualquer, encontre a quantidade de buracos nele.
    """

    contador = 0
    for char in texto.upper():
        if char in 'ADOPQR':
            contador += 1
        elif char == 'B':
            contador += 2

    return contador


if __name__ == '__main__':

    texto = '''
    Se você pensar em um papel como um plano e uma letra como uma marcação neste plano, então estas letras dividem o
    plano em regiões. Por exemplo, as letras A, D e O dividem o plano em 2 pois possuem um espaço confinado em seu
    desenho, ou um “buraco”. Outras letras como B possuem 2 buracos e letras como C e E não possuem buracos.

    Deste modo podemos considerar que o número de buracos em um texto é igual a soma dos buracos nas palavras dele.

    A sua tarefa é, dado um texto qualquer, encontre a quantidade de buracos nele.
    '''

    print('O número de buracos no texto é de: ', conta_buracos_no_texto(texto))
