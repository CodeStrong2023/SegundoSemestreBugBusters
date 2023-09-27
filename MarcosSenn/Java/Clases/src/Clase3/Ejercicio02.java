package Clase3;
import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int contador = 0;

        System.out.println("Ingresa números (teclea un número negativo para salir):");

        while (true) {
            int numero = scanner.nextInt();

            if (numero < 0) {
                break; // Salir del bucle si el número es negativo
            }

            contador++;
        }

        System.out.println("Se han introducido " + contador + " números.");

        scanner.close();
    }
}
