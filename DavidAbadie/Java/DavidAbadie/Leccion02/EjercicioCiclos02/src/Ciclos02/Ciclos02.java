/*
Ejercicio 2: Leer un número e indicar si es positivo o negativo.
El proceso se repetirá hasta que se introduzca un cero
USAMOS JOptionPane
*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
         
         int num = 0; 
        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            
            if(num > 0){
                System.out.println(num+" es POSITIVO");
            }else{
                if(num < 0){
                    System.out.println(num+" es NEGATIVO");
                }
            }
        }while(num != 0);
        System.out.println("PROGRAMA FINALIZADO");
    }
}
