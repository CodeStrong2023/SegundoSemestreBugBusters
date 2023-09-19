package clase2;

import java.util.Scanner;

public class ejercicio01 {

    public static void main(String[] args) {
        //Ciclos - Ejercicios

        //Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir
        //el proceso hasta que se introduzca un numero negativo (Clase Scanner)
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite un numero: ");
        int num = sc.nextInt();

        while (num >= 0) {
            int numCuadrado = num * num;
            System.out.println("El numero " + num + " elevado al cuadrado es: " + numCuadrado);
            System.out.println("Digite un numero: ");
            num = sc.nextInt(); 
        }
       
        System.out.println("El prgrama ha finalizado por numero negativo");
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    }

}
