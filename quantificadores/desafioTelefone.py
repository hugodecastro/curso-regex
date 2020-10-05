#coding=utf-8
import re

texto = '''Lista telefônica:
				- (11) 98756-1212
				- 98765-4321
				- (91) 98233-9325
				- 98203-8988
				- (61) 99753-8685'''

print(re.findall('\(?\d{0,2}\)?\s?\d{5}-\d{4}', texto))