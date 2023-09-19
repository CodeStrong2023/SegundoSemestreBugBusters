
package clase5;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio1 {

 
    public static void main(String[] args) {
        /*
        Ejercicio 1: Pedir un número N y mostrar todos los numeros del 1 al N. (Clase Scanner)
        */
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Digite un numero: ");
        int numN = sc.nextInt();
        
        System.out.println("Todos los numeros: ");
        for (int i = 1; i <= numN ; i++) {
            System.out.println(i);
        }
        
        
        /*
        Ejercicio 1: Pedir un número N y mostrar todos los numeros del 1 al N. (Clase JOptionPane)
        */
        
        int n = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        
        JOptionPane.showMessageDialog(null, "Todos los numeros: ");
        for (int i = 1; i <= n ; i++) {
            JOptionPane.showMessageDialog(null, i);
        }
    }
    
}
