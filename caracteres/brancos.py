import re

texto = """ca	r
r	o s!
"""

patternBrancos = re.match('ca\tr\nr\to\ss!', texto)
print("Posicoes %s, %s. Valor: %s" % (patternBrancos.start(), patternBrancos.end(),
												patternBrancos.group(0)))