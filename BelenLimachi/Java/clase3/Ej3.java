package clase3;

import javax.swing.JOptionPane;

public class Ej3 {

    public static void main(String[] args) {
         int numero;
         numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero " + numero + " ingresado es PAR");
            } 
            else {
               JOptionPane.showMessageDialog(null, "El numero " + numero + " ingresado es IMPAR"); 
                
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero:"));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " finaliza el programa"); 
     }
    
}
