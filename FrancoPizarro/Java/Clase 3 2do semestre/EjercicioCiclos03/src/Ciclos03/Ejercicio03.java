/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero
para cada uno indicar si es par o impar
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0){
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El número "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+numero+" es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showInputDialog("El número ingresado: "+numero+" finaliza el programa");
    }
    
}
