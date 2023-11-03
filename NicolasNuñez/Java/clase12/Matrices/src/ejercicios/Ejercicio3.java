
package ejercicios;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        /*
        Ejercicio 3: Leer 5 numeros por teclado, almacenarlos en un arreglo 
        y a continuación realizar la media de los números positivos, la media
        de los negativos y contar el número de ceros.
        */
        
        Scanner sc = new Scanner(System.in);
        int cantPositivos = 0;
        int cantNegativos = 0;
        double mediaPositivos = 0;
        double mediaNegativos = 0;
        int cantCeros = 0;
        
        int numeros[] = new int[5];
        //Cargar los numeros
        System.out.println("Ingrese 5 numeros: ");
        for(int i = 0; i < numeros.length; i++){
            System.out.println("Numero " + (i+1) + ": ");
            numeros[i] = sc.nextInt();
            if(numeros[i] > 0){
                mediaPositivos += numeros[i];
                cantPositivos++;
            }else if(numeros[i] < 0){
                mediaNegativos += numeros[i];
                cantNegativos++;
            }else{
                cantCeros++;
            }
        }
        
        mediaPositivos /= cantPositivos;
        mediaNegativos /= cantNegativos;
        
        
        //Mostrar los numeros
        System.out.println("Los numeros cargados son: ");
         for(int i = 0; i < numeros.length; i++){
            System.out.println("Numero " + (i+1) + ": " + numeros[i]);
        }
        System.out.println(" ");
        //Mostrar las medias
        System.out.println("Media de numeros positivos: " + mediaPositivos);
        System.out.println("Media de numeros negativos: " + mediaNegativos);
        System.out.println("Cantidad de ceros: " + cantCeros);
    }
}
