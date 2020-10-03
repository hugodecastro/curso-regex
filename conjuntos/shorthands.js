const texto = `1,2,3,4,5,6,a.b c!d?e\r	-
f_g`

console.log(texto.match(/\d/g))  // retorna todos os dígitos [0-9]
console.log(texto.match(/\D/g)) // retorna todos os não numéricos [^0-9]

console.log(texto.match(/\w/g))  // caracteres [a-zA-Z0-9_]
console.log(texto.match(/\W/g)) // não caracteres [^a-zA-Z0-9_]

console.log(texto.match(/\s/g)) // espaço [\t\n\r\t]
console.log(texto.match(/\S/g)) // não espaço [^\t\n\r\t]