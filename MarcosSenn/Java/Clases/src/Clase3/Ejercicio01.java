package Clase3;
import java.util.Scanner;

public class Ejercicio01 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa números (introduce 0 para salir):");

        while (true) {
            int numero = scanner.nextInt();

            if (numero == 0) {
                System.out.println("Saliendo del programa.");
                break;
            }

            if (numero % 2 == 0) {
                System.out.println(numero + " es un número par.");
            } else {
                System.out.println(numero + " es un número impar.");
            }
        }

        scanner.close();
    }
}
