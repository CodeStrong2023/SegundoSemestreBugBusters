 /*
Ejercicio 3: Leer numeros hasta que se introduzca un cero para cada uno.
Indicar si es par o impar. Primero lo haremos con la clase Scanner, luego 
con la clase JOptionpane
 */

package clase3;

import java.util.Scanner;

public class Ciclos03 {

    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero;
            System.out.println("Digite un numero:");
            numero = Integer.parseInt(entrada.nextLine());
            while (numero != 0) {
                if (numero % 2 == 0) {
                    System.out.println("El numero ingresado " + numero + " es par");
                } else {
                    System.out.println("El numero ingresado " + numero + " es impar");
                    
                }
                System.out.println("Digite otro numero: ");
                numero = Integer.parseInt(entrada.nextLine());
            }
            System.out.println("El numero ingresado "+ numero+ " finaliza el programa");
        } catch (NumberFormatException e) {
            
            e.printStackTrace();
        }
    }
    
}
