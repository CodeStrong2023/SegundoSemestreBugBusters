//Pedir numeros hasta que teclee un 0, mostrar la suma de todos los numeros introducidos
package Clase4;
import java.util.Scanner;

public class EjercicioSumaDeNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int suma = 0;

        System.out.println("Ingresa números o la tecla 0 para finalizar):");

        while (true) {
            int numero = scanner.nextInt();

            if (numero == 0) {
                break;
            }

            suma += numero;
        }

        System.out.println("La suma de los números es: " + suma);

        scanner.close();
    }
}
