/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,  mostrar cuantos numeros se han introducido.
Lo hacemos promero con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos04;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El número "+numero+" es POSITIVO");
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El conteo de numeros positivos introducidos es: "+conteo);
    }
}
