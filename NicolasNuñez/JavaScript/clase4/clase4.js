//Las variables son dinamicas, se pueden reutilizar 

let nombre = "Nicolas";
console.log(typeof nombre)

nombre = 21 
console.log(typeof nombre)

nombre = 12.543
console.log(typeof nombre)

let object = {
    nombre : "Nicolas",
    edad : 21,
    phoneNum : 2604111111
}

console.log(typeof object)

//Tipo de dato booleano

let boolean = true;
let bandera = false;
console.log(boolean)
console.log(bandera)

//Tipo de dato "Funcion"

function miFuncion(){
    console.log("Hola desde una funcion")
}

console.log(typeof miFuncion)

//Tipo de dato symbol

let simbolo = Symbol("Mi simbolo");
console.log(simbolo)
console.log(typeof simbolo)

//Clases 
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona)
console.log(typeof Persona)