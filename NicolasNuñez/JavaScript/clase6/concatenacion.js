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
