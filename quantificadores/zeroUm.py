import re

texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

regex = 'fogo?'

print(re.findall(regex, texto1, re.I))
print(re.findall(regex, texto2, re.I))
