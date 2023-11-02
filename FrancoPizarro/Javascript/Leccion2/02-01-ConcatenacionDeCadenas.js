var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido; // primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Bentacud'; // Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; // lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; //Aquí se puede diferenciar a través  de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera concatenacion usando el operador
console.log(nombre);

// Hoy ya no se usa avr, se utiliza let y const
let nombre2 = 'Pedro';
console.log(nombre2);

const apellido2 = 'Lepes';
//apellido2 = 'Peres'; una ctte no puede ser modificada
console.log(apellido2)

let x, y; //Se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; // Se pueden hacer asignacion de varias variables dentro de la misma línea
let z = x + y; //Se asigna el valor de la operacion
console.log(z)

let _1num = 31; //No utilizar números para iniciar una variable
let rompiendo = 'rompe'; //No utilizar palabras reseravdas para variables

console.log(_1num);
console.log(rompiendo);