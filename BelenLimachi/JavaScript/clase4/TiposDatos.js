var nombre = "Belen"; //Tipo str
console.log(nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = "3000"; 
console.log(numero);

var objeto = {
    nombre : "Belen",
    apellido : "Limachi",
    telefono : "546707"
}
console.log(objeto);
var bandera = true;
console.log(bandera);

// Tipo de Dato Funcion(Permite reutilizar líneas de código)
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de Dato Symbol
var simbolo = Symbol("Mi símbolo");
console.log(typeof simbolo);
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}