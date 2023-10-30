// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios es muy similar a la de java.
Realmente diríamos que es idéntica.
*/
var nombre = "David"; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numerico = 3000; //Tipo numeríco
console.log(numerico);

var objeto = {
    nombre : "David",
    apellido : "Abadíe",
    telefono : "2604001122"
}

console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

// Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

// Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; // null no es un un tipo de dato, pero su origen es de tipo object
console.log(y);

// Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos); // Tipo de dato object

var z = '';
console.log(z); // empty string se refiera a que es una cadena vacía, tipo string
