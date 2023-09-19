let numeros = [];

const insertarYordenar = () => {
 let numero;
 while (numero != 0) {
  numero = Number(
   prompt("Ingrese un numero mayor a 0 o presione 0 para finalizar")
  );
  numeros.push(numero);
 }
 numeros.sort((a, b) => a - b);
};
insertarYordenar();
console.log(numeros);
