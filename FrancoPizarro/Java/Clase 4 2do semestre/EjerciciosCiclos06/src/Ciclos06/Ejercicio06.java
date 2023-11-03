/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ciclos06;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ejercicio06 {
    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un número: "));
            suma += numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros ingresados es "+suma);
    }
}
