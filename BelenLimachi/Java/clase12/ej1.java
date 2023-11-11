package clase12;

import java.util.Scanner;

public class ej1 {
     public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int matriz[][] = new int[3][3];
            System.out.println("rellenar la matriz: ");
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print("matriz[" + i + "][" + j + "]: ");
                    matriz[i][j] = entrada.nextInt();

                }

            }
            System.out.println();
     
            System.out.println("matriz original: ");
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(matriz[i][j] + " ");

                }
                System.out.println();
            }
            System.out.println();
            //matriz transpuesta
            System.out.print("matriz transpuesta: ");
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(matriz[j][i] + " ");

                }
                System.out.println();
            }
        }
        System.out.println();
    }
}
