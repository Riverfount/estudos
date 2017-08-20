import requests
from bs4 import BeautifulSoup


def dados_concurso(bsObj):
    div = bsObj.find('div', {'class': 'title-bar clearfix'})
    concurso = str(div.h2).split()
    c_num = concurso[4]
    c_data = str(concurso[5])[1:11]
    return [c_num, c_data]


def parse_concurso(concurso):

    url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/' + concurso

    try:
        html = requests.request('GET', url)
    except Exception as e:
        print(f'Ocorreu o erro {e} no acesso ao site da Caixa Econômica Federal!')

    bsObj = BeautifulSoup(html.text, 'html.parser')

    return bsObj


def result_loterias(concurso, bsObj):

    nums_sorteados = []
    cells = []

    if concurso == 'lotomania' or concurso == 'lotofacil':

        if concurso == 'lotofacil':
            table = bsObj.find('table', {'class': 'simple-table lotofacil'})
        else:
            table = bsObj.table

        for row in table.findAll('tr'):
            cells.append(row.findAll('td'))

        for cell in cells:
            for i in range(len(cell)):
                nums_sorteados.append(str(cell[i])[4:6])

    elif concurso == 'megasena' or concurso == 'quina' or 'timemania':

        if concurso == 'megasena':
            classe = 'mega-sena'
        else:
            classe = concurso

        ul = bsObj.find('ul', {'class': classe})
        for i, li in enumerate(ul.findAll('li')):
            cells.append(li)
            nums_sorteados.append(str(cells[i])[4:6])

    return [concurso, nums_sorteados]


if __name__ == '__main__':
    lista_concursos = ['megasena', 'lotomania', 'quina', 'timemania', 'lotofacil']
    print(f'{" Resultado de Loteria ":=^30}')
    print('=' * 30)
    print(f'{"Menu":^30}')
    print('=' * 30)
    for i, c in enumerate(lista_concursos):
        print(f'{i + 1} - {str(lista_concursos[i]).title()}')

    ent_concurso = int(input('Qual sua opção: '))
    if ent_concurso == 1:
        tipo_concurso = 'megasena'
    elif ent_concurso == 2:
        tipo_concurso = 'lotomania'
    elif ent_concurso == 3:
        tipo_concurso = 'quina'
    elif ent_concurso == 4:
        tipo_concurso = 'timemania'
    elif ent_concurso == 5:
        tipo_concurso = 'lotofacil'

    bsObj = parse_concurso(tipo_concurso)
    concurso_num, concurso_data = dados_concurso(bsObj)

    tipo_concurso, nums_sorteados = result_loterias(tipo_concurso, bsObj)
    print('=' * 30)
    print(f'{tipo_concurso.title():^30}')
    print(f'Concurso: {concurso_num} de {concurso_data}')
    print(f'Os números sorteados foram:')
    for i, num in enumerate(nums_sorteados):
        if i in (5, 10, 15) and tipo_concurso not in ('megasena', 'timemania'):
            print()
        print(f'{num}', end = ' ')
    print()
    print('=' * 30)
