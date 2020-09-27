const texto = 'Bom\ndia'

console.log(texto.match(/.../gi))  // \n não é resolvido
console.log(texto.match(/..../gi))  // null
console.log(texto.match(/..../gis))  // a flag 's' resolve o problema do \n