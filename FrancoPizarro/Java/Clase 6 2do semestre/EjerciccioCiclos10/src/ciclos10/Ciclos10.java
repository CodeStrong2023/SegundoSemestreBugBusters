/*
Ejercicio 10: Pedir 10 números y escribir la suma total
hacerlo con la clase Scanner y JOptionPane
 */
package ciclos10;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        for(int i = 1; i <= 10; i++) {
            System.out.println("Digite un número");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        }
        System.out.println("La suma de todos los números es: "+suma);
    }
}
