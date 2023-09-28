/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ciclos01;
import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero >= 0) { //Mientras el numero sea mayor o igual a cero
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero"+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog(""));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
    
}
