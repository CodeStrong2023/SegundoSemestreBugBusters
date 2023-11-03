// Tipos de Datos en JavaScript
/*
La sintais en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre = "Ariel"; //Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof numero);
nombre = 12.3;
console.log(typeof nombre);
//Tipo Numerico
var numero = 3000; //Tipo Numérico
console.log(numero);

var objeto = {
    nombre : "Santiago",
    apellido : "Segura",
    telefono : "2604567890",
}
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion{}{}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructo(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;    
    }
}
console.log(typeof Persona);




// Tipo de dato Undef