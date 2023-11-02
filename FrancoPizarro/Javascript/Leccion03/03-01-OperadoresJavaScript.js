// Ejercicio para encontrar números pares e impares
let parInpar = 1;
if(parInpar % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if( edad >= adulto ){
    console.log('Usted es una persona adulta');
}
else{
    console.log('Usted es una persona menor de edad')
}

//Ejercicio: dentro de un rango
let dentroRango= 5;
let valMIn = 0, valMax = 10;
if (dentroRango >= valMIn && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido')
}
else{
    console.log('Esta fuera del rango establecido')
}

//Ejercicio: si el padre puede asistir al juego se su hijo
let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre no puede asistir al juego de su hijo")
}

// Operador ternario
let resultado2 = 3 > 2 ? 'verdadero':'falso';
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0 ? 'Es un número par':'Es un numero impar';
console.log(resultado2)

//convertir string a number
let miNumero = '21'; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); //esta es una funcion
console.log(typeof edad2);

//Funcion isNaN
if(isNaN(edad2)){ //No es un numero, is not a number, devuelve un resultado booleano
    console.log('Esta variable no contiene solo numeros')
}
else{
    if(edad2 >= 18){
        console.log('Puede votar');
    }
    else{
        onsole.log('Es muy joven para votar');
    }
}

//operador ternario
let resultado3 = edad2 >= 18 ? 'Puede votar':'Es muy joven para votar'
console.log(resultado3);
