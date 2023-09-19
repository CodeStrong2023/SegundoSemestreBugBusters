import java.util.Random;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Random rand = new Random();
        int numeroAleatorio = rand.nextInt(101); // Genera un número aleatorio entre 0 y 100
        int intentos = 0;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Adivina el número (entre 0 y 100): ");
            int conjetura = scanner.nextInt();

            intentos++;

            if (conjetura < 0 || conjetura > 100) {
                System.out.println("Ingresa un número entre 0 y 100.");
                continue;
            }

            if (conjetura < numeroAleatorio) {
                System.out.println("El número es mayor.");
            } else if (conjetura > numeroAleatorio) {
                System.out.println("El número es menor.");
            } else {
                System.out.println("Adivinaste en " + intentos + " intentos.");
                break;
            }
        }

        scanner.close();
    }
}
