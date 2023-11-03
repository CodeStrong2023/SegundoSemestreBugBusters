
package ciclos12;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos12 {
    public static void main(String[] args) {
        /*
        Ejercicio 2: Pedir un numero y calcular su factorial. (clase Scanner)
         */

        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese un numero para calcular su factorial: ");
        int num = sc.nextInt();
        int factorial = 1;

        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        // Otra forma
//        int factorial = num;
//        for (int i = num - 1; i > 0; i--) {
//            factorial *= i;
//        }

        System.out.println("El factorial de " + num + " es " + factorial);

        
        /*
        Ejercicio 2: Pedir un numero y calcular su factorial. (clase Scanner)
         */
        
        int num1 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero para calcular su factorial: "));
        
        int factorial1 = num1;
        for (int i = num1 - 1; i > 0; i--) {
            factorial1 *= i;
        }
        
        JOptionPane.showMessageDialog(null, "El factorial de " + num1 + " es " + factorial1);
    }
}