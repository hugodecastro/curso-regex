import re

texto = 'Casa bonita eh a casa amarela da esquina com a Rua ACASALAR.'

regex = 'casa'
patternCasa = re.findall(regex, texto, re.I)
print(patternCasa)

patternAB = re.compile('a b') 
match1 = re.search(patternAB, texto)
print("Posicoes %s, %s; Valor: %s." % (match1.start(), match1.end(), match1.group(0)))