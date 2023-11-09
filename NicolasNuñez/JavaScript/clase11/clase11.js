//DRY: Don't repeat yourself
let dias = "Sabado";
switch(dias){
    case "Lunes":
        console.log("Hoy es " + dias);
    break;
    case "Martes":
        console.log("Hoy es " + dias);
    break;
    case "Miercoles":
        console.log("Hoy es " + dias);
    break;
    case "Jueves":
        console.log("Hoy es " + dias);
    break;
    case "Viernes":
        console.log("Hoy es " + dias);
    break;
    case "Sabado":
        console.log("Hoy es " + dias);
    break;
    case "Domingo":
        console.log("Hoy es " + dias);
    break;
    case "Lunes":
        console.log("Hoy es " + dias);
    break;
    default:
        console.log("Error")
}

//Con la función no repetimos lineas de codigo y usamos menos codigo

let days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error("Out of range");
    }
    return days[n-1];
}

console.log(getDay(3));