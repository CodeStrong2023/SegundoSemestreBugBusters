
package ejercicios;

import java.util.Scanner;

public class Matriz2 {
    public static void main(String[] args) {
        /*
        Ejercicio 2: Crear una matriz de 7x7 y rellenarla de forma que los 
        elementos de la diagonal principal sean 1 y el resto 0.
        */
        
        Scanner sc = new Scanner(System.in);
        int numeros[][] = new int[7][7];
        
        System.out.println("Carga la matriz con numeros de 1 digito: ");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.println("["+i+"]["+j+"]: ");
                numeros[i][j] = sc.nextInt();
            }
        }
        
        //matriz normal
        System.out.println("\nMatriz normal");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(numeros[i][j] + " ");
            }
            System.out.println(" ");
        }     
        
        //Logica para cambiar los valores
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if(i==j){
                    numeros[i][j] = 1;
                }else{
                    numeros[i][j] = 0;
                }
            }
        }
        
        //Mostramos la matriz con la diagonal de 1
        System.out.println("\nMatriz de 0 y 1");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(numeros[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}
