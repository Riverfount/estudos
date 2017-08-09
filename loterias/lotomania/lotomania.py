import requests
from bs4 import BeautifulSoup

html = requests.request('GET', 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotomania/')

bsObj = BeautifulSoup(html.text, 'html.parser')

jogoVicente = ['07', '08', '09', '10', '13', '14', '15', '16', '17', '21', '22', '23', '24', '31', '32', '33',
               '39', '40', '45', '46', '48', '52', '53', '54', '56', '57', '58', '59', '60', '62', '63', '64',
               '66', '67', '72', '74', '75', '76', '77', '83', '84', '85', '86', '87', '91', '92', '93', '94',
               '95', '00']

jogoSileis1 = ['01', '04', '06', '08', '20', '22', '26', '29', '31', '33', '40', '43', '49', '50', '51', '52',
               '54', '55', '57', '58', '60', '61', '63', '65', '66', '69', '70', '72', '73', '74', '76', '77',
               '78', '79', '80', '81', '82', '84', '85', '86', '87', '89', '90', '91', '92', '94', '95', '97',
               '98', '99']

jogoSileis2 = ['02', '03', '05', '07', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '21',
               '23', '24', '25', '27', '28', '30', '32', '34', '35', '36', '37', '38', '39', '41', '42', '44',
               '45', '46', '47', '48', '53', '56', '59', '62', '64', '67', '68', '71', '75', '83', '88', '93',
               '96', '00']

nums_sorteados = []
res_vic = 0
res_sileis1 = 0
res_sileis2 = 0
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

for num in jogoSileis1:
    if num in nums_sorteados:
        res_sileis1 += 1

for num in jogoSileis2:
    if num in nums_sorteados:
        res_sileis2 += 1

print('=' * 42)
print(f'Concurso: {concurso_num} de {concurso_data}')
print('=' * 42 + '\n')
print(f'Vicente acertou {res_vic} números')
print('-' * 42 + '\n')
print(f'Sileis acertou {res_sileis1} números, no primeiro jogo')
print('-' * 42 + '\n')
print(f'Sileis acertou {res_sileis2} números, no segundo jogo')
print('=' * 42 + '\n')


