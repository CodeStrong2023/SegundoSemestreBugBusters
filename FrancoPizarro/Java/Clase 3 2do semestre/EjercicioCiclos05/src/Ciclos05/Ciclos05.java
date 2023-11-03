/*
Ejercicio 5: Realizar un juego para adivinar un número, para ello generar un nuúmero aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" 
según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos
 */
package Ciclos05;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        
        int numero, numAleatorio, conteo = 0;
        System.out.println("VAMOS A JUGAR");
        System.out.println("***El número aleatorio se ha generado***");
        numAleatorio = (int)(Math.random()*100); //Esto genera un númeo aleatorio
        do{
            System.out.println("Digite un número");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < numAleatorio){
                System.out.println("Digite un número MAYOR");
            }
            else if(numero > numAleatorio){
                System.out.println("Diguite un número MENOR");
            }
            else{
                System.out.println("¡FELICIDADES! Haz encontrado el número");
                System.out.println("El número era: "+numero);
            }
            conteo++;
        }while(numero != numAleatorio);
        System.out.println("Adivinaste el número en: "+conteo+" intentos");
    }
}
