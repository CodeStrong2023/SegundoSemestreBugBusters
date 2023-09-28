// Tipos de Datos en Javascript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java 
*/
var nombre = 'Flor'; // Tipo string -str-
console.log(nombre); // Imprime el valor del dato "nombre"
console.log(typeof nombre); //Imprime el tipo de dato

nombre = 7;
console.log(typeof nombre); 

nombre = 12.3;
console.log(typeof nombre); 

var numero = 3000;
console.log(numero); 

var objeto = {
    nombre: "Florencia",
    apellido: "Camona",
    edad: 34
}
console.log(objeto);

console.log(typeof objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);
console.log(typeof bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);
console.log(typeof simbolo);

// Tipo de dato clase
class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);
console.log(typeof Persona);

//Tipo de dato undefined 
var x;
console.log(x);
console.log(typeof x);

x = undefined;
console.log(x);

// null: significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es object
console.log(y);
console.log(typeof y);

//Tipo de dato array y Empty String
var juegos = ['Mario Kart 8', 'The legend of Zelda', 'Super Smash Bros.', 'Kirby Star Allies']
console.log(juegos);
console.log(typeof juegos);

var z = '';
console.log(z); //cadena vacia
console.log(typeof z);

