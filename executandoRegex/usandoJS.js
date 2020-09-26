const texto = '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f'

const regexNove = RegExp('9')
console.log('métodos da RegExp...')
console.log(regexNove.test(texto))
console.log(regexNove.exec(texto))

const regexLetras = /[a-f]/g
console.log('métodos da string...')
console.log(texto.match(regexLetras))
console.log(texto.search(regexLetras)) // retorna o índice do primeiro elemento que foi encontrado
console.log(texto.replace(regexLetras, 'Achei'))
console.log(texto.split(regexLetras))