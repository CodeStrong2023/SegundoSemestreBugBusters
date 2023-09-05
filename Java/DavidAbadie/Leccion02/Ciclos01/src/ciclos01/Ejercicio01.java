package ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int num, cuadrado;
        
        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));

            cuadrado = (int)Math.pow(num, 2);
            if (num >= 0) {
                System.out.println(num + "^2 = " + cuadrado);
            }
            
        }while(num >= 0);
        System.out.println("PROGRAMA FINALIZADO");
    }
} 