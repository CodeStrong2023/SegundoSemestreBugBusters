/*
Ejercicio 2: Leer un número e indicar si es positivo o negativo.
El proceso se repetirá hasta que se introduzca un cero
*/
package Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num = 0; 
        do{
            System.out.println("Ingrese un número: ");
            num = entrada.nextInt();
            if(num > 0){
                System.out.println(num+" es POSITIVO");
            }else{
                if(num < 0){
                    System.out.println(num+" es NEGATIVO");
                }
            }
        }while(num != 0);
        System.out.println("PROGRAMA FINALIZADO");
    }
}
