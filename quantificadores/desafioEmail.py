#coding=utf-8
import re

texto = '''Os emails dos convidados são:
				- fulano@cod3r.com.br
				- xico@gmail.com
				- isadoracarlapinto@gmail.com.br
				- caleboliverfabiodacunha@keffin.com
                - maria_silva@registro.br
				- rafa.sampaio@yahoo.com'''

print(re.findall('[\w.]+@\w+.\w{2,4}.?\w{0,2}', texto))