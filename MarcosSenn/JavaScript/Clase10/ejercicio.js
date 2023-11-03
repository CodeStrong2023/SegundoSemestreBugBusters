//estaciones del año
function estacion(mes) {
    if (mes == 12 || mes == 1 || mes == 2) {
        return "Verano";
    }
    if (mes == 3 || mes == 4 || mes == 5) {
        return "Otoño";
    }
    if (mes == 6 || mes == 7 || mes == 8) {
        return "Invierno";
    }
    if (mes == 9 || mes == 10 || mes == 11) {
        return "Primavera";
    }
}

console.log(estacion(10));

//hora del dia
var horaActual = new Date().toLocaleTimeString();
console.log(`Son las ${horaActual}`);

//switch con brake

const consultarEstacion = (mes) => {
    switch (mes) {
        case 1:
        case 2:
        case 12:
            return "verano";
        case 3:
        case 4:
        case 5:
            return "otoño";
        case 6:
        case 7:
        case 8:
            return "invierno";
        case 9:
        case 10:
        case 11:
            return "primavera";
        default:
            return "mes incorrecto";
            break;
    }
};

console.log(consultarEstacion(10));
