/*
Ejercicio 8: pedir un número N, y mostrar todos los números
del 1 al N
 */
package Ciclo08;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ejercicio08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}
