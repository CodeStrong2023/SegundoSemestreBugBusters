/*
Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos clases, Scanner y JOptionPane
 */
package ciclos12;

import javax.swing.JOptionPane;

public class Ejercicio12 {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Ingresa un número para calcular su factorial:");
        int numero = Integer.parseInt(input);

        int factorial = calcularFactorial(numero);

        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }

    public static int calcularFactorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * calcularFactorial(n - 1);
        }
    }
}
  
