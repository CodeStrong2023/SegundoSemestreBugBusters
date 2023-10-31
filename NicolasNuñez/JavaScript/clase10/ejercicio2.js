//Hora del día
/**
 de 6 a 11: morning
 de 12 a 16: afternoon
 de 17 a 19: evening
 de 20 a 23: night
 */

 hora = 15;
 mensaje = null;

 if(hora >= 6 && hora <= 11){
    mensaje = "Good morning";
 }else if(hora >= 12 && hora <= 16){
    mensaje = "Good afternon";
 }else if(hora >= 17 && hora <= 19){
    mensaje = "Good evening";
 }else if(hora >= 20 && hora <= 23){
    mensaje = "Good night";
 }else{
    mensaje = "Hora invalida"
 }

 console.log(mensaje)