
package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio1 {

    
    public static void main(String[] args) {
        
        /*
        Ejercicio 1: Pedir numeros hasta que se teclee un 0,
        mostrar la suma de todos los numeros introducidos. (Clase Scanner).
        */
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingrese un numero: ");
        int num = sc.nextInt();
        int suma = 0;
        
        while(num != 0){
           suma = suma + num;
           System.out.println("Ingrese otro numero: ");
           num = sc.nextInt();
        }
        
        System.out.println("El programa ha finalizado por introducir un cero");
        System.out.println("La suma de los numeros introducidos da: " + suma);
        
        
        /*
        Ejercicio 1: Pedir numeros hasta que se teclee un 0,
        mostrar la suma de todos los numeros introducidos. (Clase JOptionPane).
        */
        
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        int sumaNums = 0;
        
        while(num2 != 0){
            sumaNums = sumaNums + num2;
            num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        }
        
        JOptionPane.showMessageDialog(null, "El programa ha finalizado por introducir un cero");
        JOptionPane.showMessageDialog(null, "La suma de los numeros introducidos da: " + sumaNums);
    }
    
}
