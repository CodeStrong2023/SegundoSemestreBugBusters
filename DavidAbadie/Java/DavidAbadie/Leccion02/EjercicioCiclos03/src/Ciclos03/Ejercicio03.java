/*
Ejercicio 3: Leer números hasta que se introduzzca un cero.
Para cada uno indicar si es par o impar.
Primero se hará con la clase Scanner y luego con las cale JOptionPane
*/
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(num != 0){ 
            if(num % 2 == 0){
                System.out.println(num +" es PAR");
            }else{
                System.out.println(num +" es IMPAR");
            }
            
            System.out.println("Ingrese un número: ");
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        }
        System.out.println("PROGRAMA FINALIZADO");
    }
}

