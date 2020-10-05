import re

texto = '<div>Conteudo 01</div><div>Conteudo 02</div>'

print(re.findall('<div>.+<\/div>', texto))
print(re.findall('<div>.*<\/div>', texto))
print(re.findall('<div>.{0,100}<\/div>', texto))

print(re.findall('<div>.+?<\/div>', texto))
print(re.findall('<div>.*?<\/div>', texto))
print(re.findall('<div>.{0,100}?<\/div>', texto))