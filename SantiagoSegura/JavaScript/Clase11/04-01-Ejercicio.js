// Ejercicio 1: Calcular estacion del año

function calcularEstacion() {
    const fecha = new Date();
    const mes = fecha.getMonth();
  
    let estacion;
  
    if (mes === 11 || mes === 0 || mes === 1) {
      estacion = "Invierno";
    } else if (mes >= 2 && mes <= 4) {
      estacion = "Primavera";
    } else if (mes >= 5 && mes <= 7) {
      estacion = "Verano";
    } else if (mes >= 8 && mes <= 10) {
      estacion = "Otoño";
    } else {
      estacion = "Error";
    }
  
    return estacion;
  }
  
  const estacionActual = calcularEstacion();
  console.log(`La estación actual es: ${estacionActual}`);
  

// Ejercicio 2: Hora del día

/* 
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Godd afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 no saluda: Good night
Trabajaremos con 24 horas
*/

function saludarSegunHora(hora) {
    let saludo;
  
    if (hora >= 6 && hora <= 11) {
      saludo = "Good Morning";
    } else if (hora >= 12 && hora <= 16) {
      saludo = "Good Afternoon";
    } else if (hora >= 17 && hora <= 19) {
      saludo = "Good Evening";
    } else if (hora >= 20 && hora <= 23) {
      saludo = "Good Night";
    } else {
      saludo = "Hora no válida";
    }
  
    return saludo;
  }
  
  const horaActual = new Date().getHours();
  const saludo = saludarSegunHora(horaActual);
  
  console.log(saludo);
  

  //Estructura switch (la sintaxis es igual a Java)
  function calcularEstacion() {
    const fecha = new Date();
    const mes = fecha.getMonth();
  
    let estacion;
  
    switch (mes) {
      case 11:
      case 0:
      case 1:
        estacion = "Invierno";
        break;
      case 2:
      case 3:
      case 4:
        estacion = "Primavera";
        break;
      case 5:
      case 6:
      case 7:
        estacion = "Verano";
        break;
      case 8:
      case 9:
      case 10:
        estacion = "Otoño";
        break;
      default:
        estacion = "Error";
        break;
    }
  
    return estacion;
  }
  
  const estacionActual = calcularEstacion();
  console.log(`La estación actual es: ${estacionActual}`);
  
  //Evitar repetir tu codigo
  //Dry don't repeat yourself
 // let days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
  let days = 5;
  switch (days){
    case 1:
      console.log('Hoy es lunes')
      break;
      
    case 2:
      console.log('Hoy es martes')
    break;

    case 3:
      console.log('Hoy es miercoles')
      break;
      
    case 4:
      console.log('Hoy es jueves')
    break;

    case 5:
      console.log('Hoy es viernes')
      break;
      
    case 6:
      console.log('Hoy es sabado')
    break;

    case 7:
      console.log('Hoy es domingo')
    break;
  }
// Esta es una version mejorada 

   let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
   function getDay(n){
    if(n < 1 || n > 7){
      throw new Error('out of range');
    }
    return days2[n-1];
   }
   console.log(getDay(5));

   //Hacer un ejercicio similar al que esta hecho, pero ahora con los
   //meses del año, debes hacerlo con la estructura switch y luego 
   //con la funcion en la opcion mejorada

   function obtenerNombreMesSwitch(numero) {
    let nombreMes;
    switch (numero) {
        case 1:
            nombreMes = "Enero";
            break;
        case 2:
            nombreMes = "Febrero";
            break;
        case 3:
            nombreMes = "Marzo";
            break;
        case 4:
            nombreMes = "Abril";
            break;
        case 5:
            nombreMes = "Mayo";
            break;
        case 6:
            nombreMes = "Junio";
            break;
        case 7:
            nombreMes = "Julio";
            break;
        case 8:
            nombreMes = "Agosto";
            break;
        case 9:
            nombreMes = "Septiembre";
            break;
        case 10:
            nombreMes = "Octubre";
            break;
        case 11:
            nombreMes = "Noviembre";
            break;
        case 12:
            nombreMes = "Diciembre";
            break;
        default:
            nombreMes = "Mes inválido";
            break;
    }
    return nombreMes;
}

let mes = 6; // Colocar el numero de mes requerido
let nombreMes = obtenerNombreMesSwitch(mes);
console.log(nombreMes);

//Opcion mejorada

function obtenerNombreMesFuncion(numero) {
  const meses = ["Enero", "Febrero", "Marzo", "Abril","Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"];

  if (numero >= 1 && numero <= 12) {
      return meses[numero - 1];
  } else {
      return "Mes inválido";
  }
}

let mes = 6; // Colocar el numero de mes requerido
let nombreMes = obtenerNombreMesFuncion(mes);
console.log(nombreMes);




