const lista1 = [
 "manzana",
 "pera",
 "banana",
 "naranja",
 "hamster",
 "tortuga",
 "kiwi",
];
const lista2 = [
 "perro",
 "gato",
 "conejo",
 "loro",
 "hamster",
 "tortuga",
 "pera",
];

//1 Lista de palabras que aparecen en las listas
const ambasListas = [...lista1, ...lista2];
console.log(ambasListas);

//2 Lista de palabras que aparecen en la primer lista pero no en la segunda
const primeraYnoEnSegunda = lista1.filter((palabra) => {
 return !lista2.includes(palabra);
});
console.log(primeraYnoEnSegunda);

//3 Lista de palabras que aparecen en la segunda lista pero no en la primera
const segundaYnoPrimera = lista2.filter((palabra) => {
 return !lista1.includes(palabra);
});
console.log(segundaYnoPrimera);

//4 Lista de palabras que aparecen en ambas listas
const palabrasEnAmbasListas = lista1.filter((palabra) => {
 return lista2.includes(palabra);
});
console.log(palabrasEnAmbasListas);
