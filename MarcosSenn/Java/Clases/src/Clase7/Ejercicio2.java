package Clase7;
import javax.swing.JOptionPane;
import java.util.Scanner;

public class Ejercicio2 {
    //factorial de un numero con JOptionPane
    public static void main(String[] args){
        String numero = JOptionPane.showInputDialog("Ingrese un numero para calcular su factorial");
        int num = Integer.parseInt(numero);
       System.out.println( factorial(num));
    }
    public static int factorial(int num){
        if(num == 0){
            return 1;
        }
        if(num ==1){return 1;}
        return num * factorial(num - 1);
    }
}