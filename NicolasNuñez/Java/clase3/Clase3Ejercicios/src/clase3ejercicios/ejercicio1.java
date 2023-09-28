package clase3ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio1 {

    public static void main(String[] args) {

        /*
        Ejercicio 1: Leer números hasta que se introduzca un cero. 
        Para cada uno indicar si es par o impar. (clase Scanner)
         */
       
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite un numero: ");
        int num = sc.nextInt();

        while (num != 0) {
            if (num % 2 == 0) {
                System.out.println("El numero " + num + " es par");
                System.out.println("Digite otro numero: ");
                num = sc.nextInt();

            } else {
                System.out.println("El numero " + num + " es impar");
                System.out.println("Digite otro numero: ");
                num = sc.nextInt();
            }
        }
        System.out.println("El programa ha finalizado debido al numero cero");
        
        
        /*
        Ejercicio 1: Leer números hasta que se introduzca un cero. 
        Para cada uno indicar si es par o impar. (clase JOptionPane)
         */
        
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        
        while(num2 != 0){
            if(num2 % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero " + num2 + " es par");
                num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            }else{
                JOptionPane.showMessageDialog(null, "El numero " + num2 + " es impar");
                num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            }
        }
        JOptionPane.showMessageDialog(null, "El programa ha finalizado debido al numero cero");
    }

}
