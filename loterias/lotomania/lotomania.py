import requests
from bs4 import BeautifulSoup

html = requests.request('GET', 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotomania/')

bsObj = BeautifulSoup(html.text, 'html.parser')

jogoVicente = ['07', '08', '09', '10', '13', '14', '15', '16', '17', '21', '22', '23', '24', '31', '32', '33',
               '39', '40', '45', '46', '48', '52', '53', '54', '56', '57', '58', '59', '60', '62', '63', '64',
               '66', '67', '72', '74', '75', '76', '77', '83', '84', '85', '86', '87', '91', '92', '93', '94',
               '95', '00']

nums_sorteados = []
res_vic = 0
cells = []

table = bsObj.table

div = bsObj.find('div', {'class': 'title-bar clearfix'})
concurso = str(div.h2).split()
concurso_num = concurso[4]
concurso_data = str(concurso[5])[1:11]

for row in table.findAll('tr'):
    cells.append(row.findAll('td'))

for cell in cells:
    for i in range(len(cell)):
        nums_sorteados.append(str(cell[i])[4:6])


for num in jogoVicente:
    if num in nums_sorteados:
        res_vic += 1

print('\n\n\n'+ '=' * 42)
print(f'Concurso: {concurso_num} de {concurso_data}'.center(42))
print('=' * 42 + '\n')
print('-' * 42)
print(f' Vicente acertou {res_vic} números '.center(42))
print('-' * 42 + '\n')
print('=' * 42 + '\n\n\n')

