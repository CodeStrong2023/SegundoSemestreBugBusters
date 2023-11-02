/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos
numeros se han introducido.
 */

package clase3;

import java.util.Scanner;

public class Ciclos04 {

      public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero;
            int contador = 0;
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            while (numero > 0) {
                System.out.println("El numero " + numero + " es POSITIVO");
                contador++;
            System.out.println("Digite otro numero:");
            numero = Integer.parseInt(entrada.nextLine());

            }
            System.out.println("A ingresado "  + contador + " numeros que no son negativos");
        } catch (NumberFormatException e) {
            
            e.printStackTrace();
        }
    }
}