
package ciclowhile;

public class EjercicioWhile01 {

    public static void main(String[] args) {
        //Ciclo while = ciclo mientras
        var conteo = 0; //Inferencia de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        //Uso de las palabras break y continue junto a las etiquetas (labels)
        inicio:
        for(var cont = 0; cont < 7; cont++ ){
            if(cont % 2 == 0){
                System.out.println("cont = " + cont);
             break inicio;
            }
        }
        
        for(var cont = 0; cont < 7; cont++ ){
            if(cont % 2 != 0){
                continue;
            }
             System.out.println("cont = " + cont);
        }
         
        
    }
    
}
