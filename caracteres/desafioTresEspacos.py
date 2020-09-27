import re

TEXTO = 'a   b'
PRINT_TEXT = "Posicoes %s, %s; Valor: %s."

patternEspaco1 = re.match('a   b', TEXTO)
print('a   b: ', PRINT_TEXT % (patternEspaco1.start(), patternEspaco1.end(),
                                             patternEspaco1.group(0)))
patternEspaco2 = re.match('a\s\s\sb', TEXTO)
print('a\s\s\sb: ', PRINT_TEXT % (patternEspaco2.start(), patternEspaco2.end(),
                                             patternEspaco2.group(0)))
patternEspaco3 = re.match('a...b', TEXTO)
print('a...b: ', PRINT_TEXT % (patternEspaco3.start(), patternEspaco3.end(),
                                             patternEspaco3.group(0)))
patternEspaco4 = re.match('a\s+b', TEXTO)
print('a\s+b: ', PRINT_TEXT % (patternEspaco4.start(), patternEspaco4.end(),
                                             patternEspaco4.group(0)))
patternEspaco5 = re.match('a {3}b', TEXTO)
print('a {3}b: ', PRINT_TEXT % (patternEspaco5.start(), patternEspaco5.end(),
                                             patternEspaco5.group(0)))
patternEspaco6 = re.match('a\s{3}b', TEXTO)
print('a\s{3}b: ', PRINT_TEXT % (patternEspaco6.start(), patternEspaco6.end(),
                                             patternEspaco6.group(0)))