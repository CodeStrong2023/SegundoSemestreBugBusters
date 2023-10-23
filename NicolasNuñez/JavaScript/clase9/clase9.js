//Operador ternario 

let resultado = 3 > 2 ? "verdadero" : "falso";
console.log(resultado);

//Ejercicio: numero par
let num = 4;
let numPar = (num % 2 == 0) ? `${num} es par` : `${num} es impar`;
console.log(numPar)

//Convertir String a Number
let miNumero = "15"; 
console.log(typeof miNumero);
let edad = Number(miNumero);
console.log(edad)
console.log(typeof edad)

//Funcion isNaN
if(isNaN(edad)){
    console.log("La variable no es un numero");
}else{
    if(edad >= 16){
        console.log("Puedes votar");
    }else{
        console.log("Eres demasiado joven para votar");
    } 
}

let resultado2 = (edad >= 16) ? "Puedes votar" : "Eres demasiado joven para votar";
console.log(resultado2);


