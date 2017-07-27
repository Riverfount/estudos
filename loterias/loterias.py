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
    html = requests.request('GET', url)
    bsObj = BeautifulSoup(html.text, 'html.parser')

    return bsObj


def result_loterias(concurso, bsObj):

    nums_sorteados = []
    cells = []

    if concurso == 'lotomania':

        table = bsObj.table

        for row in table.findAll('tr'):
            cells.append(row.findAll('td'))

        for cell in cells:
            for i in range(len(cell)):
                nums_sorteados.append(str(cell[i])[4:6])

    elif concurso == 'megasena':

        ul = bsObj.find('ul', {'class': 'numbers mega-sena'})
        for i, li in enumerate(ul.findAll('li')):
            cells.append(li)
            nums_sorteados.append(str(cells[i])[4:6])
        '''
        for i, cell in enumerate(cells):
            nums_sorteados.append(str(cell[i])[4:6])
        '''
    return [concurso, nums_sorteados]


if __name__ == '__main__':

    print('Resultado de Loteria')
    ent_concurso = int(input('Você quer saber o resultado de qual loteria (1) Mega-Sena (2) Lotomania: '))
    if ent_concurso == 1:
        concurso = 'megasena'
    else:
        concurso = 'lotomania'
    bsObj = parse_concurso(concurso)
    concurso_num, concurso_data = dados_concurso(bsObj)

    concurso, nums_sorteados = result_loterias(concurso, bsObj)
    print('=' * 30)
    print(concurso.upper())
    print(f'Concurso: {concurso_num} de {concurso_data}')
    print(f'Os números sorteados foram:')
    for i, num in enumerate(nums_sorteados):
        if i in (5, 10, 15) and concurso != 'megasena':
            print()
        print(f'{num}', end = ' ')
    print()
    print('=' * 30)
