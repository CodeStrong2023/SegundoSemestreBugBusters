/*
Ejercicio 8: pedir un número N, y mostrar todos los números
del 1 al N
 */
package Ciclo08;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Ciclo08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
