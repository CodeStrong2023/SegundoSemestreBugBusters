
package Ciclos06;

import javax.swing.JOptionPane;


public class Ejercicio06 {
    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            suma += numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los números ingresados es: "+suma);
    
    }
}
