package Clase12;

public class MatrizTranspuesta {
    public static void main(String[] args) {
        int[][] matrizOriginal = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        int[][] matrizTranspuesta = new int[3][3];

        // Transponer la matriz
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrizTranspuesta[i][j] = matrizOriginal[j][i];
            }
        }

        // Mostrar la matriz original
        System.out.println("Matriz Original:");
        mostrarMatriz(matrizOriginal);

        // Mostrar la matriz transpuesta
        System.out.println("Matriz Transpuesta:");
        mostrarMatriz(matrizTranspuesta);
    }

    public static void mostrarMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
