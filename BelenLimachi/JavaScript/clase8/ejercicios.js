var nombre = "";
nombre = "Walter";
console.log(nombre);
function saludar(){
    var nombre3 = "Brisa";
    console.log(nombre3);
}
//console.log(nombre3);//no lee el dato en la funcion
if (true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);//En la funcion funciono correctamente en la estructura if fallo
/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/
function saludar2(){
    let nombre2 = "Martin";
    console.log(nombre2);
}
//console.log(nombre2);
if(true){
    let edad2 = 38;
    console.log(edad2);
}
//console.log(edad2);
/*
const se utiliza para valores constantes que no pueden ser reasignadas*/
const fechanacimiento = 2001;
console.log(fechanacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento);// Solo se ejecuta el console anterior