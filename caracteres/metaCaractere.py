import re

texto = '1,2,3,4,5,6,a.b c!d?e'

patternPonto = re.split('\.', texto)
print(patternPonto)

patternSymbol = re.split(',|\.|\?|!| ', texto)
print(patternSymbol)