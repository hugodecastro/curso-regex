const texto = '<div>Conteudo 01</div><div>Conteudo 02</div>'

// quantificadores são greedy

console.log(texto.match(/<div>.+<\/div>/g))
console.log(texto.match(/<div>.*<\/div>/g))
console.log(texto.match(/<div>.{0,100}<\/div>/g))

// quantificadoes não greedy
console.log(texto.match(/<div>.+?<\/div>/g))  // ? torna a regez lazy (não greedy)
console.log(texto.match(/<div>.*?<\/div>/g))
console.log(texto.match(/<div>.{0,100}?<\/div>/g))