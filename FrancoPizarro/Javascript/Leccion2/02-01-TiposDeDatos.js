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