import re

texto = """1,2,3,4,5,6,a.b c!d?e\r	-
f_g"""

print(re.findall('\d', texto))
print(re.findall('\D', texto))

print(re.findall('\w', texto))
print(re.findall('\W', texto))

print(re.findall('\s', texto))
print(re.findall('\S', texto))