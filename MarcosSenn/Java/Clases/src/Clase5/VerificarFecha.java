package Clase5;
import java.util.Scanner;

public class VerificarFecha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el día: ");
        int dia = scanner.nextInt();

        System.out.print("Ingresa el mes: ");
        int mes = scanner.nextInt();

        System.out.print("Ingresa el año: ");
        int anio = scanner.nextInt();

        boolean fechaCorrecta = verificarFecha(dia, mes, anio);

        if (fechaCorrecta) {
            System.out.println("La fecha ingresada es correcta.");
        } else {
            System.out.println("La fecha ingresada es incorrecta.");
        }

        scanner.close();
    }

    public static boolean verificarFecha(int dia, int mes, int anio) {
        if (mes < 1 || mes > 12 || dia < 1 || dia > 30) {
            return false;
        }

        if (mes == 2) {

            if (anio % 4 == 0) {

                if (dia > 29) {
                    return false;
                }
            } else {

                if (dia > 28) {
                    return false;
                }
            }
        }

        return true;
    }
}
