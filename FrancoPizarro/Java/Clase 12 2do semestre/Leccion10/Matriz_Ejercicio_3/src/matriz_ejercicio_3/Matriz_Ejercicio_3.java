/*
Ejercicio 3: Crear y cargar una matriz de tamaño 3*3, transponerla  mostrarla
 */
package matriz_ejercicio_3;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][]= new int [3][3];
        
        System.out.println("Digite numeros para rellenar la matriz de 3*3");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Matriz ["+i+"] ["+j+"] : ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println(); //Salto de linea
        
        System.out.println("Matriz Original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
        
        System.out.println("Matriz transpuesta: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
