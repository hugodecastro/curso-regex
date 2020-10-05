#coding=utf-8
import re

texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

regex = 'fogo+'

print(re.findall(regex, texto1, re.I))
print(re.findall(regex, texto2, re.I))

texto3 = 'Os números : 0123456789.'

print(re.findall('\d', texto3))
print(re.findall('\d+', texto3))
