package clase6;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio {

    public static void main(String[] args) {
        /*
       Ejercicio 1: Pedir 10 numeros y escribir la suma total.
       (Clase Scanner)
         */

        Scanner sc = new Scanner(System.in);
        System.out.println("Debe ingresar 10 numeros");
        int suma = 0;
        for(int i = 0; i < 10; i++){
            System.out.println((i+1) + ": Ingrese un numero: ");
            int num = sc.nextInt();
            suma += num;
        }
        
        System.out.println("La suma total de los 10 numeros da: " + suma);

        
        /*
       Ejercicio 1: Pedir 10 numeros y escribir la suma total.
       (Clase JOptionPane)
         */
        
        JOptionPane.showMessageDialog(null, "Debe ingresar 10 numeros");
        int suma = 0;
        for (int i = 0; i < 10; i++) {
            int num = Integer.parseInt(JOptionPane.showInputDialog((i + 1) + ": Ingrese un numero: "));
            suma += num; 
        }
        JOptionPane.showMessageDialog(null, "La suma total de los 10 numeros da: " + suma);
    }

}
