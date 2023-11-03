package ejercicios;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        int numeros[] = new int[5];
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese 5 numeros: ");
        for(int i = 0; i < numeros.length; i++){
            System.out.println("Numero " + (i+1) + ": ");
            numeros[i] = sc.nextInt();
        }

        System.out.println("Los numeros cargados son: ");
        for(int i = 0; i < numeros.length; i++){
            System.out.println("Numero " + (i+1) + ": " + numeros[i]);
        }
    }
}






