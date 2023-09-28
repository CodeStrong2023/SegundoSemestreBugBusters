
package ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio1 {
    public static void main(String[] args) {
        /*
        Ejercicio 1: Diseñar un programa que muestre el producto de los 10 primeros numeros impares.
        Hacerlo con la clase JOptionPane
        */
        
        int producto = 1;
        for (int i = 0; i < 20; i++) { //int i = 1; i <= 20; i+=2
            if(i % 2 == 1){
                producto *= i;
            }
            
        }
        
        JOptionPane.showMessageDialog(null, "El producto de los numeros impares es: " + producto);
    }
}
