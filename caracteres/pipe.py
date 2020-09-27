import re

texto = 'Voce precisa responder sim, nao ou nao sei'

print(re.findall('sim|nao|sei', texto))