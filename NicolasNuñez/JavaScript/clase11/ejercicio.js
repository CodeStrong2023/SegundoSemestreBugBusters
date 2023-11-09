let mes = 8;
//switch: 

switch(mes){
    case 1:
        console.log("Enero");
    break;
    case 2:
        console.log("Febrero");
    break;
    case 3:
        console.log("Marzo");
    break;
    case 4:
        console.log("Abril");
    break;
    case 5:
        console.log("Mayo");
    break;
    case 6:
        console.log("Junio");
    break;
    case 7:
        console.log("Julio");
    break;
    case 8:
        console.log("Agosto");
    break;
    case 9:
        console.log("Septiembre");
    break;
    case 10:
        console.log("Octubre");
    break;
    case 11:
        console.log("Noviembre");
    break;
    case 12:
        console.log("Diciembre");
    break;
    default:
        console.log("Error. Número de mes incorrecto.");
}


//Función: 

let meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

function getMonth(x){
    if(x < 1 || x > 12){
        throw new Error("Out of range");
    }else{
        return meses[x - 1];
    }
}

console.log(getMonth(5))