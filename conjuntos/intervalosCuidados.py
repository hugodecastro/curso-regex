import re

texto = 'ABC [abc] a-c 1234'

print(re.findall('[a-c]', texto))
print(re.findall('a-c', texto))
print(re.findall('[A-z]', texto))