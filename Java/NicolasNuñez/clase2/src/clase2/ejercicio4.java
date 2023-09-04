
package clase2;

import javax.swing.JOptionPane;

public class ejercicio4 {
    public static void main(String[] args) {
        /* Ejercicio 2: Leer un numero e indicar si es positivo o negativo.
            El proceso se repitira hasta que se introduzca un cero. (Clase Scanner)
         */
        
        int num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        
        while (num != 0) {
            if (num > 0) {
                JOptionPane.showMessageDialog(null, "El numero " + num + " es positivo");
                num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

            } else if (num < 0) {
                JOptionPane.showMessageDialog(null, "El numero " + num + " es negativo");
                num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            }
        }
        JOptionPane.showMessageDialog(null, "El prgrama ha finalizado por el numero cero");
    }
}
