/*
Ejercicio 3: Leer 5 numeros por teclado, almacenarlos en
un arreglo y a continuacion realizar la media de los 
numeros positivos, la media de los negativos y contar el
numero de ceros.
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_Ejercicio_3 {
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[5];
        int sumaPositivos = 0, sumaNegativos = 0, contadorCeros = 0;
        int contadorPositivos = 0, contadorNegativos = 0;

        // Leer los 5 números
        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i+1) + ": ");
            numeros[i] = scanner.nextInt();

            if (numeros[i] > 0) {
                sumaPositivos += numeros[i];
                contadorPositivos++;
            } else if (numeros[i] < 0) {
                sumaNegativos += numeros[i];
                contadorNegativos++;
            } else {
                contadorCeros++;
            }
        }

        // Calcular medias
        double mediaPositivos = contadorPositivos > 0 ? (double) sumaPositivos / contadorPositivos : 0;
        double mediaNegativos = contadorNegativos > 0 ? (double) sumaNegativos / contadorNegativos : 0;

        System.out.println("Media de números positivos: " + mediaPositivos);
        System.out.println("Media de números negativos: " + mediaNegativos);
        System.out.println("Número de ceros: " + contadorCeros);
    }
}
    
    

