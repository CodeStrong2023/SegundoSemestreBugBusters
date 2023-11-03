/*
var, let y const

var: es la forma antigua de declarar variables, se puede reasignar en cualquier momento.
let: es la forma moderna de declarar variables, , se puede reasignar en cualquier momento
    Ambito de bloque: Solo disponible dentro de un bloque de llaves o dentro de una función.
const: es la forma moderna de declarar variables que no van a cambiar 

var: es una variable global
let: es una variable local
const: es una variable local
*/

let nombre = "David";
const apellido = "Abadie";
var edad = 22;

function imprimirNombre(nombre) {
    var edad = 30;
    var nombre = "David";
    console.log(`Tengo ${edad} años`);
    console.log(`Me llamo ${nombre} ${apellido}`);

    if (edad > 10) {
        var nombre = "Ricardo";
        console.log(`Me llamo ${nombre} ${apellido}`);
    }

    console.log(nombre);
}

imprimirNombre(nombre);

console.log(edad);