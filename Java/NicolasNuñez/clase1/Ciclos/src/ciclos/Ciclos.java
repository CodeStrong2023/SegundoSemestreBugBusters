package ciclos;

public class Ciclos {

    public static void main(String[] args) {
        //Ciclo while
        System.out.println("While:");

        int conteo = 0;

        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //incrementa de a uno
        }
        
        System.out.println(" ");
        
        //Ciclo do-while
        System.out.println("Do-While:");

        int contador = 0;
        do { //ejecuta al menos una vez el codigo

            System.out.println("contador = " + contador);
            contador++; //incrementa de a uno la variable

        } while (contador <= 7);
        
        System.out.println(" ");
        
        //Ciclo for
        System.out.println("For: ");
        
        for(int i = 0; i <= 7; i++){
            System.out.println("i = " + i);
            
        }
        
        System.out.println(" ");
        
        
        //palabras break - continue
        
        //break -> rompe la ejecución del ciclo
        
        System.out.println("Break: ");
        for (int i = 0; i <= 10; i++) {
            if(i % 2 == 0){
                System.out.println(i);
                break;
            }
        }
        
        //continue -> salta dicha vuelta del iterador y continua con la ejecución del programa
        
        System.out.println("Continue: ");
        for (int i = 0; i <= 10; i++) {
            if(i % 2 != 0){
                continue;
            }
            System.out.println(i);  
        }
        
        System.out.println(" ");
        
        //Labels - etiquetas -> se convinan con las palabras break-continue (no se recomienda usar)
        
        System.out.println("Labels: ");
        
        inicio:
         for (int i = 0; i <= 10; i++) {
            if(i % 2 == 0){
                System.out.println(i);
                break inicio;
            }
        }
        
        System.out.println(" ");
        
        inicio2:
         for (int i = 0; i <= 10; i++) {
            if(i % 2 != 0){
                continue inicio2;
            }
            System.out.println(i);  
        }
    }

}
