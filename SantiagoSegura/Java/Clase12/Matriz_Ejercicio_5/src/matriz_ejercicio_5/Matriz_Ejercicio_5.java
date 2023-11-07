/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y cada columna.
 */
package matriz_ejercicio_5;

import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args){        
        int n = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de filas (n):"));
        int m = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de columnas (m):"));

        int[][] matriz = new int[n][m];

        // Pedir al usuario que ingrese los valores de la matriz
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                String valor = JOptionPane.showInputDialog("Ingrese el valor para la fila " + (i + 1) + " y columna " + (j + 1) + ":");
                matriz[i][j] = Integer.parseInt(valor);
            }
        }

        // Calcular y mostrar 
        String sumaFilas = "Suma de filas:\n";
        for (int i = 0; i < n; i++) {
            int sumaFila = 0;
            for (int j = 0; j < m; j++) {
                sumaFila += matriz[i][j];
            }
            sumaFilas += "Fila " + (i + 1) + ": " + sumaFila + "\n";
        }

        // Calcular y mostrar 
        String sumaColumnas = "Suma de columnas:\n";
        for (int j = 0; j < m; j++) {
            int sumaColumna = 0;
            for (int i = 0; i < n; i++) {
                sumaColumna += matriz[i][j];
            }
            sumaColumnas += "Columna " + (j + 1) + ": " + sumaColumna + "\n";
        }

        JOptionPane.showMessageDialog(null, sumaFilas + "\n" + sumaColumnas);
    }
}

    
    


    
    

