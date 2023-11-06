/*
Ejercicio 1: Leer 5 numeros, guardados en un arreglo y
mostrarlos en el mismo orden introducidos.
 */


package arreglos_ejercicio_1;

import java.util.Scanner;

public class Arreglos_Ejercicio_1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[5];

        // Leer los 5 números
        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i+1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        System.out.println("Los números introducidos son:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
        }
    }
}

    
}
