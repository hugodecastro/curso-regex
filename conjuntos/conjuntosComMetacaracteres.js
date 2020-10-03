const texto = '.$+*?-'

console.log(texto.match(/[+.?*$]/g))  // dentro do conjunto a maioria dos
                                      // metacaracteres são literais
console.log(texto.match(/[$-?]/g))  // intervalo válido
console.log(texto.match(/[$\-?]/g)) // não é um intervalo
console.log(texto.match(/[-?]/g))
