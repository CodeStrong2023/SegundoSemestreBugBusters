import java.util.Scanner;

public class mostrarDeUnoAN {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa un número (n): ");
        int n = scanner.nextInt();

        if (n <= 0) {
            System.out.println("El número debe ser un entero positivo.");
        } else {
            System.out.println("Números del 1 al " + n + ":");
            for (int i = 1; i <= n; i++) {
                System.out.print(i + " ");
            }
        }

        scanner.close();
    }
}