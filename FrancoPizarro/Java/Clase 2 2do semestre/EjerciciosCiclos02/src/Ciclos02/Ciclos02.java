/*
 Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso se repetira hasta
que se introduzca un 0 con la clase JOptionPane
 */
package Ciclos02;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ciclos02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if (numero > 0){
                System.out.println("El numero "+numero+" es POSITIVO");
            }
            else{
                System.out.println("El numero "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("Usted oprimio el numero "+numero+", el programa finalizo");
    }
}
