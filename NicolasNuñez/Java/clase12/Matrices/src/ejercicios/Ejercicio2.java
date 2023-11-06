
package ejercicios;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        /*
        Ejercicio 1: Leer 5 numeros, guardarlos en un arreglo y 
        mostrarlos en el orden inverso al introducidos. 
        */
        
        int numeros[] = new int[5];
        Scanner sc = new Scanner(System.in);
        
        //Cargar los numeros
        System.out.println("Ingrese 5 numeros: ");
        for(int i = 0; i < numeros.length; i++){
            System.out.println("Numero " + (i+1) + ": ");
            numeros[i] = sc.nextInt();
        }
        
        //Mostrar los numeros en el orden invertido
        System.out.println("Los numeros cargados son: ");
         for(int i = numeros.length - 1; i >= 0; i--){
            System.out.println("Numero " + (i+1) + ": " + numeros[i]);
        }
    }
 
}
