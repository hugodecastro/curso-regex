# -*- coding: utf-8 -*-

import re

texto = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46'

print(re.findall('\d{1,2}', texto))
print(re.findall('[0-9]{2}', texto))
print(re.findall('\d{1,2}', texto))

print(re.findall('\d{1,}', texto))
print(re.findall('\w{7}', texto))

print(re.findall(r'[\wõ]{7,}', texto.decode('utf-8'), re.UNICODE))


print(re.findall('\b\d{1,2}\b', texto,))
print(re.findall('\b[\wõ]{7}\b', texto))