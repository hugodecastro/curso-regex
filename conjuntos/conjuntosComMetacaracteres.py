import re

texto = '.$+*?-'

print(re.findall('[+.?*$]', texto))
print(re.findall('[$-?]', texto))
print(re.findall('[$\-?]', texto))
print(re.findall('[-?]', texto))
