package clase11;

import java.util.Scanner;

public class Ej2 {
    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            float numeros[]=new float[5];
            System.out.println("guardando los elementos del arreglo: ");
            for (int i = 0; i < 5; i++) {
                System.out.println((i+1)+" digite un numero: ");
                numeros[i]=entrada.nextFloat();
                          
            }
            System.out.println("\nimprimimos los elementos del arreglo: ");
            for (int i = 4; i >=0; i--) {
                System.out.println(" "+numeros[i]);
                
            }
        }
        System.out.println("\n");
    }
}
