/*
Ejercicio 4: Pedir número hasta que se teclee uno negativo,
y mostrar cuántos números se han introducio.
clase JOption Pane
*/
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {
        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
         int contador = 0;
        while(num >= 0){
            contador++; // Nos muestra cuantos numeros se han introducido
            System.out.println("Ingrese un número: ");
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        }
        System.out.println("Se ingresaron "+ contador +" números positivos. ");
    }   
}