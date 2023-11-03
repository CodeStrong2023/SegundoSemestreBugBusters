package clase6;

import javax.swing.JOptionPane;

public class Ej10 {
    public static void main(String[] args) {
        
        int numero, suma = 0;
        for(int i = 1; i <= 10; i++){
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;
            
        }
    JOptionPane.showMessageDialog(null, "La suma de todos los numeros es: " +suma);
    }      
     
}
