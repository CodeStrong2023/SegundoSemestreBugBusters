/*
Ejercicio: 3: Crear y cargar una matriz de tamaño 3x3, transponerla y mostrarla
 */
package matriz_ejercicio_3;

public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        int matrizOriginal[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int matrizTranspuesta[][] = new int[3][3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrizTranspuesta[i][j] = matrizOriginal[j][i];
            }
        }
        System.out.println("Rellenar Matriz:");
        mostrarMatriz(matrizOriginal);

        System.out.println("\nMatriz Transpuesta:");
        mostrarMatriz(matrizTranspuesta);
    }

    public static void mostrarMatriz(int[][] matriz) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}

        
 


