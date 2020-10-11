#coding:utf-8
import re

texto = 'Pedrinho (filho de Pedro Silva) é doutor do ABC!'

print(re.findall(r'[(abc)]', texto, re.I))
print(re.findall(r'([abc])', texto, re.I))
print(re.findall(r'(abc)', texto, re.I))