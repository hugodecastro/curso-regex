import re

texto = 'supermercado hipermercado minimercado mercado'

print(re.findall(r'((hiper|super|mini)?mercado)', texto))
print(re.findall(r'((hi|su)per|mini)?mercado', texto))