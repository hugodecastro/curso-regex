#coding:utf-8
import re

texto1 = '<b>Destaque</b><strong>Forte</strong><div>Conteudo</div>'
print(re.findall(r'\<(\w+)\>.*\<\/\1\>', texto1, re.I))

texto2 = 'Lentamente é mente muito lenta'
print(re.findall(r'(lenta)(mente).*\2.*\1', texto2, re.I))
print(re.findall(r'(?:lenta)(mente).*\1', texto2, re.I))

print(re.findall(r'(lenta)(mente)', texto2, re.I))
print(re.findall(r'(lenta)(mente)?', texto2, re.I))
print(re.sub(r'(lenta)(mente)', texto2, r'\2'))
