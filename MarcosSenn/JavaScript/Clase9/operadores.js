//algfunos operadores

let vacaciones = true
let diaDescanso = false
let plata = false

if(vacaciones || diaDescanso){console.log("Vamos a un viaje")}
if(vacaciones || diaDescanso && plata){console.log("Vamos a un viaje")}
(vacaciones && plata)? console.log("Vamos a un viaje") : console.log("No vamos a ningun lado")

!plata ? console.log("No vamos a ningun lado, no hay palta") : console.log("Vamos de viaje") 



//NaN

const esNumero = (n) => {
    console.log(isNaN(n) ? "No es un numero" : "Es un numero")
}

esNumero("hola")
esNumero(4)