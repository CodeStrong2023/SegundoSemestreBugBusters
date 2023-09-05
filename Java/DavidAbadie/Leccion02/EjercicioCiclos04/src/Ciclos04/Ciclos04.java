/*
Ejercicio 4: Pedir número hasta que se teclee uno negativo,
y mostrar cuántos números se han introducio.
clase Scanner
*/
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); 
        System.out.println("Ingrese un número: ");
        int num = entrada.nextInt();
        int contador = 0;
        while(num >= 0){
            contador++; // Nos muestra cuantos numeros se han introducido
            System.out.println("Ingrese un número: ");
            num = entrada.nextInt();
        }
        System.out.println("Se ingresaron "+ contador +" números positivos. ");
    }
}
