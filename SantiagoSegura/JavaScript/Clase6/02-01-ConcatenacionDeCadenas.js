var nombre = 'Jose ';
var apellido = 'Montes ';
var nombreCompleto = nombre+''+apellido; //Primera Concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+''+'Betancud'; //Segunda Concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izquierda a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; //Aquí se puede diferencia a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos); 

nombre += apellido //Tercera Concatenación usando el operador simplificado
console.log(nombre);

