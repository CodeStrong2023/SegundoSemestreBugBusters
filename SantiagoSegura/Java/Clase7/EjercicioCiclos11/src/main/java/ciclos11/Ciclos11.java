/*
Ejercicio 11: Diseñar un programa que muestre el proyecto 
de los 10 primeros numeros impares
hacerlo con JOptionPane
 */
package ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {    
    public static void main(String[] args) {
        String resultado = "Los primeros 10 números impares son:\n";

        for (int i = 1; i <= 20; i += 2) {
            resultado += i + "\n";
        }
        JOptionPane.showMessageDialog(null, resultado);
    }
}

