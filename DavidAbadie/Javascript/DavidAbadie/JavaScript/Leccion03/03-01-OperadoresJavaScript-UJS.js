//Ejercicio para encontrar números pares
const parImpar = (num) => {
    if(num % 2 === 0){
        console.log('par');
    }else{
    console.log('impar');
    }
}

parImpar(21); // cambiar el numero

//Ejercicio: es mayor de edad
const esMayorOmenor = (edad) => {
    if(edad>=18){
        console.log("Es mayor de edad");
    }else{
        console.log("Es menor de edad");
    } 
}

esMayorOmenor(50); // cambiar el numero

//Ejercicio: Dentro de un rango
let dentroRango = 5; //Cambiar valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango");
}
else{
    console.log("Esta fuera del rango");
}
