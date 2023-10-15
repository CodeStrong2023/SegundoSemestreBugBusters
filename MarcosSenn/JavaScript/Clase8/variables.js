// var let y const

// var es la forma antigua de declarar variables
// let es la forma moderna de declarar variables
// const es la forma moderna de declarar variables que no van a cambiar

// var es una variable global
// let es una variable local
// const es una variable local

let nombre = "Sacha";
const apellido = "Lifszyc";
var edad = 28;

function imprimirNombre(nombre) {
    var edad = 30;
    var nombre = "Milano";
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
