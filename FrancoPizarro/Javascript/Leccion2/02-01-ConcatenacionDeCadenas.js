var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido; // primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Bentacud'; // Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; // lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; //Aquí se puede diferenciar a través  de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera concatenacion usando el operador
console.log(nombre);