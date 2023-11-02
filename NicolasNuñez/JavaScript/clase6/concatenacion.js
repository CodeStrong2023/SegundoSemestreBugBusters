let nombre = "Nicolas";
let apellido = "Nuñez"

let nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto)

let nombreCompleto2 = "Ariel" + " " + "Betancud";
console.log(nombreCompleto2)

let juntos = nombre + 219; //Lee de izq a der siguiendo la cadena, lee el numero como str
console.log(juntos)

juntos = nombre + 78 + 12;
console.log(juntos)

juntos = 78 + 12 + nombre;
console.log(juntos)

nombre += apellido;
console.log(nombre)

//Hoy ya no se usa var, se utiliza let
let nombre2 = "Pedro";
console.log(nombre2);

//usamos const para constantes

const apellido2 = "Lepes";
// apellido2 = "Nuñez"; NO se puede modificar
console.log(apellido2)

//Ampliando el uso de var let y const

/*
Con var puedes reasignar en cualquier momento. Esta forma
parte del ambito global.
Un error es que se sobreescriba 
 */

var nombre3 = "Ariel";
nombre3 = "Osvalodo";
console.log(nombre3);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
console.log(nombre3) //Aquí no lee el dato en la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad) //En la función funcionó correctamente, en la estructura if falló


/*
let: esta puede ser reasignada en cualquier momento. La diferencia es que su ambito
es de bloque, solo disponible dentro de un bloque de llaves o dentro de una función
*/

function saludar2(){
    let nombre4 = "Ariel";
    console.log(nombre4)
}
//console.log(nombre4)

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2)

/*
const: se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2002;
console.log(fechaNacimiento);
//fechaNacimiento = 2006;
console.log(fechaNacimiento); //solo se ejecuta el console anterior
