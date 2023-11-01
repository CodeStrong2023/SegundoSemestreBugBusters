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

//Ejercicio: Si el padre puede asistir al juego de su hijo

let vacaciones = false, diaDescanso = true;
if(vacaciones || diaDescanso){
    console.log("El padre si puede asisitir al juego de su hijo");
}else{
    console.log("El padre NO puede asistir al juego de su hijo");
}

//Operador ternario 
//(para codigo corto) similar al if else
let resultado = 3 > 2 ? "verdadero" : "falso";
console.log(resultado);

//Ejercicio: numero par
let num = 6;
let numPar = (num % 2 == 0) ? `${num} es par` : `${num} es impar`;
console.log(numPar)

//Convertir String a Number
let miNumero = "17"; //Es una cadena
console.log(typeof miNumero);
let edad = Number(miNumero);//Es una funcion
console.log(edad)
console.log(typeof edad)

//Funcion isNaN (is not a number = no es un numero) (Boolean)
if(isNaN(edad)){
    console.log("La variable no es un numero");
}else{
    if(edad >= 16){
        console.log("Puedes votar");
    }else{
        console.log("Eres demasiado joven para votar");
    } 
}
//Operador ternario
let resultado2 = (edad >= 16) ? "Puedes votar" : "Eres demasiado joven para votar";
console.log(resultado2);