/*
Ejercicio 1: Leer 5 números, guardarlos en un arreglo y mostrarlos en el mismo orden introducidos
 */
package arreglos_ejercicios_1;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Arreglos_Ejercicios_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] arreglos = new float [5];
        
        System.out.println("Escriba un número para el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+" . Digite un número");
            arreglos[i] = entrada.nextInt();
        }
        
        System.out.println("Los números de los arreglos son: ");
        for(float i:arreglos){
            System.out.println(i+" ");
        }
        System.out.println("\n");
    }
}