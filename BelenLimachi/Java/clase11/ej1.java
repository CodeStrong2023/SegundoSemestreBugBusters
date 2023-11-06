package clase11;

import java.util.Scanner;

public class ej1 {
     public static void main(String[] args) {

        float[] numeros = new float[5];

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }
        System.out.println("Los números introducidos son:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
        }

        scanner.close();//aca cierro el scanner 
    }
}
