
package clase3ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class ejercicio2 {
    public static void main(String[] args) {
        /*
        Ejercicio 2: Pedir numeros hasta que se teclee uno negativo y mostar
        cuantos numeros se han introducido. (clase Scanner)
        */
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Digite un numero: ");
        
        int num = sc.nextInt();
        int contador = 0;
        
        while(num >= 0){
            System.out.println("El numero " + num + " es positivo");
            System.out.println("Digite otro numero: ");
            num = sc.nextInt();
            contador++;
        } 
        System.out.println("El programa ha finalizado debedio a un numero negativo");
        System.out.println("Se ha introducido " + contador + " numeros positivos");
        
        
        /*
        Ejercicio 2: Pedir numeros hasta que se teclee uno negativo y mostar
        cuantos numeros se han introducido. (clase JOptionPane)
        */
        
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int contadorNum = 0;
        
        while(num2 >= 0){
            JOptionPane.showMessageDialog(null, "El numero " + num2 + " es positivo");
            num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            contadorNum++;
        }
        JOptionPane.showMessageDialog(null, "El programa ha finalizado debedio a un numero negativo");
        JOptionPane.showMessageDialog(null, "Se ha introducido " + contadorNum + " numeros positivos");
        
    }
}
