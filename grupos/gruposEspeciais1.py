import re

texto = 'Joao eh calmo, mas no transito fica nervoso.'

print(re.findall(r'[\w]+', texto, re.IGNORECASE))

print(re.findall(r'[\w]+(?=,)', texto, re.IGNORECASE))
print(re.findall(r'[\w]+(?=\.)', texto, re.IGNORECASE))

print(re.findall(r'[\w]+\b(?!,)', texto, re.IGNORECASE))
print(re.findall(r'[\w]+[\s|\.](?!,)', texto, re.IGNORECASE))