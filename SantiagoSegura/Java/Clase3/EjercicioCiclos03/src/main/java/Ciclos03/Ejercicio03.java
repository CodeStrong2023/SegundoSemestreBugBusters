/*
Eejercicio 3: Leer numeros hasta que se introduzca un cero
Para cada uno identificar si es par o impar
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if (numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es IMPAR"); 
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite OTRO numero: "));
        }
        JOptionPane.show.MessageDialog(null, "El numero ingresado es "+numero+" finaliza el programa");
        
    }
    
}
