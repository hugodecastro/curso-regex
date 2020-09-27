const texto = 'a   b'

console.log('/a   b/: ', texto.match(/a   b/))
console.log('/a\s\s\sb/: ',texto.match(/a\s\s\sb/))
console.log('/a...b/: ',texto.match(/a...b/))

console.log('/a\s+b/: ',texto.match(/a\s+b/))
console.log('/a {3}b/: ',texto.match(/a {3}b/))
console.log('/a\s{3}b/: ',texto.match(/a\s{3}b/))