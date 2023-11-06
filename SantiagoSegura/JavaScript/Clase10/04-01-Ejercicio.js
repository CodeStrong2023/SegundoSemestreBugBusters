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
  
  
