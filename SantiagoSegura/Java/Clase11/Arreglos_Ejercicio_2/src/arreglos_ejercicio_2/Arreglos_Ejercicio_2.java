/*
Ejercicio 2: Leer 5 numeros, guardarlos en un arreglo y
mostrarlos en el orden inverso al introducirlos.
 */

package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[5];

        // Leer los 5 números
        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i+1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        System.out.println("Los números introducidos en orden inverso son:");
        for (int i = 4; i >= 0; i--) {
            System.out.println(numeros[i]);
        }
    }
}
    

