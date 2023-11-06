// Ejercicio 1: Calcular la estacion del año

let mesActual = 1;
if(mesActual == 12 || mesActual == 1 || mesActual == 2){
    console.log('Usted se encuentra en la estación de VERANO');
}
else if(mesActual == 3 || mesActual == 4 || mesActual == 5){
    console.log('Usted se encuentra en la estación de OTOÑO');
}
else if(mesActual == 6 || mesActual == 7 || mesActual == 8){
    console.log('Usted se encuentra en la estación de INVIERNO');
}
else if(mesActual == 9 || mesActual == 10 || mesActual == 11){
    console.log('Usted se encuentra en la estación de PRIMAVERA');
} 
else{
    console.log('Esta estación no existe')
}

// Ejercicio 2: Hora del día
let horaDia = 1;
let parteDelDia;
if(horaDia >= 7 && horaDia <= 11 ){
    parteDelDia = 'la Mañana';
}
else if(horaDia >= 12 && horaDia <= 16){
    parteDelDia = 'el Mediodía';
}
else if(horaDia >= 17 && horaDia <= 20){
    parteDelDia = 'la Tarde';
}
else if(horaDia >= 21 && horaDia <= 24){
    parteDelDia = 'la Noche';
}
else if(horaDia >= 1 && horaDia <= 6){
    parteDelDia = 'la madrugada'
}
else{
    console.log('Esta parte del día no existe');
}
console.log('La hora es '+horaDia+' y es '+parteDelDia);

// Estructura switch(la sintaxis es igual a Java)
switch(mesActual){//No solo se pueden utilizar número, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano"
        break;

    case 3: case 4: case 5:
        estacion = "Otoño"
        break;

    case 6: case 7: case 8:
        estacion = "Invierno"
        break;
   
    case 9: case 10: case 11:
        estacion = "Primavera"
        break;

    default:
        estacion = "Valor incorrecto"
}
console.log('Bienvenido a la estación de: '+estacion)