//Calcular estación del año

mes = 4

switch(mes){
    case 1: case 2: case 3:
        console.log("La estación del año es Verano");
        break;
    case 4: case 5: case 6:
        console.log("La estación del año es Otoño");
        break;
    case 7: case 8: case 9:
        console.log("La estación del año es Invierno");
        break;
    case 10: case 11: case 12:
        console.log("La estación del año es Primavera");
        break;
    default:
        console.log("Número de mes invalido");
}