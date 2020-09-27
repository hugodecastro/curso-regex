import re

texto = 'Bom\ndia'

print(re.findall('...', texto, re.DOTALL))
print(re.findall('....', texto, re.DOTALL))