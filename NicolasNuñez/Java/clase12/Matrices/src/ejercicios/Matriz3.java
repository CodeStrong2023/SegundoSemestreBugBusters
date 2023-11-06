package ejercicios;

import java.util.Scanner;

public class Matriz3 {

    /*
    Ejercicio 3: Crear y cargar una matriz de tamaño n x m, mostrar la suma de 
    cada fila y de cada columna.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sumaFila, sumaCol, posFila, posCol;

        System.out.println("Ingrese la cantidad de filas: ");
        int fila = sc.nextInt();

        System.out.println("Ingrese la cantidad de columnas: ");
        int col = sc.nextInt();

        int numeros[][] = new int[fila][col];
        int filas[] = new int[fila];
        int columnas[] = new int [col];
        

        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < col; j++) {
                System.out.println("[" + i + "][" + j + "]: ");
                numeros[i][j] = sc.nextInt();
            }
        }

        //mostramos la matriz
        System.out.println("\nMatriz cargada");
        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(numeros[i][j] + " ");
            }
            System.out.println(" ");
        }
        
        //Sumamos las filas
        posFila = 0;
        for (int i = 0; i < fila; i++) {
            sumaFila = 0;
            for (int j = 0; j < col; j++) {
                sumaFila += numeros[i][j];
            }
            filas[posFila] = sumaFila;
            posFila++;
        }
        
        //Sumamos las columnas
        posCol = 0;
        for (int j = 0; j < col; j++) {
            sumaCol = 0;
            for (int i = 0; i < fila; i++) {
                sumaCol += numeros[i][j];
            }
            columnas[posCol] = sumaCol;
            posCol++;
        }
        
        System.out.println("\nLa suma de las filas es: ");
        for (int i = 0; i < fila; i++) {
            System.out.print(filas[i] + "-");
        }
        
        System.out.println("\nLa suma de las columnas es: ");
        for (int i = 0; i < col; i++) {
            System.out.print(columnas[i] + "-");
        }
        System.out.println(" ");
    }

}
