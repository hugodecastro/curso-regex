import re

texto = '1,2,3,4,5,6,a.b c!d?e[f'

print(re.findall('[a-z]', texto))
print(re.findall('[b-d]', texto))
print(re.findall('[2-4]', texto))
print(re.findall('[A-Z1-3]', texto, re.I))
