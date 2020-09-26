// g - global -> procura por todos os caracteres que correspodem
// i - ignore case -> ignora letras maiúsculas e minúsculas

const texto = 'Carlos assinou o abaixo-assinado.'
console.log(texto.match(/C|ab/)) // retorna apenas o primeiro caractere encontrado
console.log(texto.match(/c|ab/i))
console.log(texto.match(/ab|c/gi)) // retorna todos os caracteres que correspondem a pesquisa