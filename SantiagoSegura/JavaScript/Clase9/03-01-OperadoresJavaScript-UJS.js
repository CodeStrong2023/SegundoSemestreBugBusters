// Ejercicio para encontrar numeros pares
let parInpar = 10;
if(parInpar % 2 == 0){
	console.log("Es un numero PAR");
}
else{
	console.log("Es un numero INPAR");
}

// Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if(edad >= adulto){
	console.log("Usted es una persona adulta");
}
else{
	console.log("Usted es una persona menor de edad")
}

let dentroRango = 5;
let valMin = 0;
let valMax = 10;

if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log('Está dentro del rango establecido');
} else {
    console.log('Está fuera del rango establecido');
}

//Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = falso;
if(vacaciones || diaDescanso){
	console.log("El padre puede asistir al juego de su hijo")
}
else{
	console.log("El padre no puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un numero INPAR"

//Convertir String a Number
let miNumero = "10"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); // Esta es una funcion
console.log(typeof edad2);

//Funcion isNaN
if(isNaN(edad2)){ //No es un numero
	console.log("Esta variable no contiene solo numeros")
}
else{
	
}
if(edad2 >= 18){
	console.log("Puede votar");
}
else{
	console.log("Muy joven para votar")
}







