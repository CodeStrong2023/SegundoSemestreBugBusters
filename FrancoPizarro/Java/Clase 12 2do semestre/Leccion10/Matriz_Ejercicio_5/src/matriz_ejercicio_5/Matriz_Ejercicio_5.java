/*
Ejercicio 5: Crear y cargar una matriz de tamaño n * m, mostrar la suma de cada fila y de cada columna
 */
package matriz_ejercicio_5;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Matriz_Ejercicio_5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        
        int matriz[][], nFilas, nColumnas, sumaFilas, sumaCol;
        int posFila, posColumna;
        
        System.out.print("Digite el tamaño de filas que quiere la matriz: ");
        nFilas = entrada.nextInt();
        System.out.print("Digite el tamaño de columnas que quiere la matriz: ");
        nColumnas  = entrada.nextInt();
        
        matriz = new int [nFilas][nColumnas];
        int filas[] = new int [nFilas];
        int columnas[] = new int [nColumnas];
        
        System.out.println("Vamos a rellenar la matriz: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nColumnas; j++) {
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
        System.out.println("\nMatriz original: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nColumnas; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        System.out.println("");
        
        //Suma de Filas
        posFila = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFilas = 0;
            for (int j = 0; j < nColumnas; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[posFila] = sumaFilas;
            posFila++;
        }
        
        //Sumando columnas
        posColumna = 0;
        for (int j = 0; j < nColumnas; j++) {
            sumaCol = 0;
            for (int i = 0; i < nFilas; i++) {
                sumaCol += matriz[i][j];
            }
            columnas[posColumna] = sumaCol;
            posColumna++;
        }
        
        System.out.println("\nLa suma de las filas: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.print(filas[i]+" - ");
        }
        System.out.println("");
        System.out.println("\nLa suma de columnas es: ");
        for (int i = 0; i < nColumnas; i++) {
            System.out.print(columnas[i]+" - ");
        }
        System.out.println("");
    }
}
