package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio2 {

    public static void main(String[] args) {
        /*
        Ejercicio 2: Pedir numeros hasta que se introduzca uno negativo y calcular la media. (Clase Scanner)
         */

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int num = sc.nextInt();
        int contador = 0;
        int suma = 0;
        double media = 0;
        while (num >= 0) {
            suma = suma + num;
            contador++;
            System.out.println("Ingrese otro numero: ");
            num = sc.nextInt();
        }
        
        if(contador == 0){
            System.out.println("Error! La division entre cero no existe");
        }else{
            media = (float)suma / contador;
            System.out.println("El programa ha finalizado por introducir un numero negativo");
            System.out.println("La media de los numeros introducidos da: " + media);
        }
                
        /*
        Ejercicio 2: Pedir numeros hasta que se introduzca uno negativo y calcular la media. (Clase JOptionPane)
        */
       
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        int sumaNums = 0;
        int contadorNums = 0;
        double media2 = 0;
        
        while(num2 >= 0){
            sumaNums = sumaNums + num2;
            contadorNums++;
            num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        }
        
        if(contadorNums == 0){
            JOptionPane.showMessageDialog(null, "Error! La division entre cero no existe");
        }else{
            media2 = (float)sumaNums / contadorNums;
            JOptionPane.showMessageDialog(null, "El programa ha finalizado por introducir un numero negativo");
            JOptionPane.showMessageDialog(null, "La media de los numeros introducidos da: " + media2);
        }
    }
}
