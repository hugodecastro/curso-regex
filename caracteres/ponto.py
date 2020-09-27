import re

texto = '1,2,3,4,5,6,7,8,9,0'
PRINT_TEXT = "Posicoes %s, %s; Valor: %s."

patternNums1 = re.match('1.2', texto)
print(PRINT_TEXT % (patternNums1.start(), patternNums1.end(),
                                         patternNums1.group(0)))

patternNums2 = re.match('1..2', texto)
if patternNums2 is not None:
    print(PRINT_TEXT % (patternNums2.start(), patternNums2.end(),
                                         patternNums2.group(0)))
else:
    print(None)

patternNums3 = re.match('1..,', texto)
print(PRINT_TEXT % (patternNums3.start(), patternNums3.end(),
                                         patternNums3.group(0)))

notas = '8.3,7.1,8.8,10.0'

patternNotas = re.match('8..', notas)
print("Posicoes %s, %s; Valor: %s." % (patternNotas.start(), patternNotas.end(),
                                         patternNotas.group(0)))

patternNotas2 = re.findall('.\..', notas)
print(patternNotas2)