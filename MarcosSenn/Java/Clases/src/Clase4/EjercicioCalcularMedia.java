package Clase4;
import java.util.Scanner;

public class EjercicioCalcularMedia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int suma = 0;
        int contador = 0;

        System.out.println("Ingresa números o teclea un número negativo para finalizar):");

        while (true) {
            int numero = scanner.nextInt();

            if (numero < 0) {
                break;
            }
            suma += numero;
            contador++;
        }
        if (contador == 0) {
            System.out.println("No se introdujeron números.");
        } else {
            double media = (double) suma / contador;
            System.out.println("La media de los números es: " + media);
        }
        scanner.close();
    }
}
