/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y mostrarlos en el orden inverso
al introducido
 */
package arreglos_ejercicio_2;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float[] numeros = new float [5];
        
        System.out.println("Escriba los números para los arreglos");
        for (int i = 0; i < 5; i++) {
            System.out.print((i+1)+". Digite el valor para el arreglo: ");
            numeros[i] = entrada.nextInt();
        }
        System.out.println("Los valores del arreglo al inverso son: ");
        for (int i = 5; i > 0; i--) {
            System.out.println(i + " ");
        }
        System.out.println("\n");
    }
}
