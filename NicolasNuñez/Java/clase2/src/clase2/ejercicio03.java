package clase2;

import java.util.Scanner;

public class ejercicio03 {

    public static void main(String[] args) {
        /* Ejercicio 2: Leer un numero e indicar si es positivo o negativo.
            El proceso se repitira hasta que se introduzca un cero. (Clase Scanner)
         */

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite un numero: ");
        int num = sc.nextInt();

        while (num != 0) {
            if (num > 0) {
                System.out.println("El numero " + num + " es positivo");
                System.out.println("Digite un numero: ");
                num = sc.nextInt();

            } else if (num < 0) {
                System.out.println("El numero " + num + " es negativo");
                System.out.println("Digite un numero: ");
                num = sc.nextInt();
            }
        }
        System.out.println("El prgrama ha finalizado por el numero cero");
    }
}
