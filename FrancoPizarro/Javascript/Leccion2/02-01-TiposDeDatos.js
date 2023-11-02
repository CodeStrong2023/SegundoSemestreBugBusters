// Tipos de datos en JavaScript
/* 
La sintaxis en lo que es comentarios es muy similar  a la
de Java, realmente diriamos que es identica
*/
//Tipo String
var nombre = "Franco"; //Tipo String
console.log(typeof nombre);
nombre = 7;
console.log(nombre);
nombre = 12.3;
console.log(typeof nombre);
//Tipo numerico
var edad = 19;
console.log(edad);
//Tipo Object
var objeto = {
    nombre : "Franco",
    apellido : "Pizarro",
    telefono : "2604817007"
}
console.log(typeof objeto);

// Tipo de dato boolean (se las conoce como bandera)
var bandera = true;
console.log(bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol("MI SIMBOLO");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona)

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; // null no es un tipo de dato pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y empty String
var autos = ['Citroen','Audi','BMW','Ford','Chevrolet']
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es

var z = '';
console.log(z); // Esto se refiere a que es una cadena vacia
console.log(typeof z)
