package Clase12;

import java.util.Scanner;

public class SumaFilasColumnasMatriz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el número de filas (n): ");
        int n = scanner.nextInt();

        System.out.print("Ingrese el número de columnas (m): ");
        int m = scanner.nextInt();

        int[][] matriz = new int[n][m];

        // Cargar la matriz con valores
        cargarMatriz(matriz, scanner);

        // Mostrar la matriz
        System.out.println("Matriz ingresada:");
        mostrarMatriz(matriz);

        // Calcular y mostrar la suma de cada fila
        for (int i = 0; i < n; i++) {
            int sumaFila = 0;
            for (int j = 0; j < m; j++) {
                sumaFila += matriz[i][j];
            }
            System.out.println("Suma de la fila " + (i + 1) + ": " + sumaFila);
        }

        // Calcular y mostrar la suma de cada columna
        for (int j = 0; j < m; j++) {
            int sumaColumna = 0;
            for (int i = 0; i < n; i++) {
                sumaColumna += matriz[i][j];
            }
            System.out.println("Suma de la columna " + (j + 1) + ": " + sumaColumna);
        }
    }

    public static void cargarMatriz(int[][] matriz, Scanner scanner) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Ingrese el valor para la posición [" + i + "][" + j + "]: ");
                matriz[i][j] = scanner.nextInt();
            }
        }
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
