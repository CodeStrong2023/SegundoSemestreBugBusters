/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,  mostrar cuantos numeros se han introducido.
Luego con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while(numero >= 0) {
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }
        JOptionPane.showMessageDialog(null, "El conteo de números POSITIVOS es "+conteo);
    }
    
}
