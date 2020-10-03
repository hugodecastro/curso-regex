import re

texto = '1,2,3,a.b c!d?e[f'

print(re.findall('\D', texto))
print(re.findall('[^0-9]', texto))
print(re.findall('[^\d!?\[\s,.]', texto))

texto2 = '1: !"#$%&\'()*+,-./ 2: :;<=>?@'

print(re.findall('[^!-/:-@\s]', texto2))