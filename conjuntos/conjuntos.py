import re

texto = '1,2,3,4,5,6,a.b c!d?e[f'

print(re.findall('[02468]', texto))

texto2 = 'Joao nao vai passear na moto.'

print(re.findall('n[aa]', texto2))