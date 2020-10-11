#coding=utf-8
import re

texto1 = 'O José Simão é muito engraçado... hehehehehe'
print(re.findall(r'((he)+)', texto1))

texto2 = 'http://www.site.info www.escola.ninja.br google.com.ag'
print(re.findall('((http:\/\/)?(www\.)?\w+\.\w{2,}(\.\w{2})?)+', texto2))
