/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y luego ir pidiendo
números indicando "es mayor" o "es menor" según sea mayor o menor
con respecto a N.
El proceso termina cuando el usuario acierta y mostramos el número
de intentos hechos.
*/
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int num, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100); // Genera un numero aleatorio
        
        do{
            System.out.println("Adivine el número: ");
            num = entrada.nextInt();
            if(num > aleatorio){
                System.out.println("ES MAYOR");
            }else if(num < aleatorio){
                System.out.println("ES MENOR");
            }else{
                System.out.println("\t¡¡¡FELICIDADES!!! Has adivinado el número :)");
            }
            contador++;
        }while(num != aleatorio);   
        System.out.println("\tAdivinaste el número en: "+contador+" intentos");
    }
}
