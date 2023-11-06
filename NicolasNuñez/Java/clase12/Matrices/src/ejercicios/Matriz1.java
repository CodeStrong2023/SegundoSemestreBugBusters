
package ejercicios;

import java.util.Scanner;

public class Matriz1 {
    public static void main(String[] args) {
        /*
        Ejercicio 1: crear y cargar una matriz de 3x3, transponerla y mostrarla
        */
        
        Scanner sc = new Scanner(System.in);
        int numeros[][] = new int[3][3];
        
        System.out.println("Carga la matriz con numeros de 1 digito: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("["+i+"]["+j+"]: ");
                numeros[i][j] = sc.nextInt();
            }
        }
        
        //matriz normal
        System.out.println("\nMatriz normal");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(numeros[i][j] + " ");
            }
            System.out.println(" ");
        }
        
        System.out.println("\nMatriz transpuesta");
        //Transponemos la matriz y la mostramos
        for (int j = 0; j < 3; j++) {
            for (int i = 0 ; i < 3; i++) {
                System.out.print(numeros[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}
