/*
Ejercicio 9: Pedir el día, mes y año de una fecha e
indicar si la fecha es correcta. Suponiendo que
todos los meses son 30 dias.
 */
package Ciclos09; 

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        int año = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        if((dia != 0)&& (dia <= 30)){
            if((mes != 0)&&(mes <= 12)){
                if((año != 0)&&(año <= 2023)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + año);
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
        }
    }
    else{
        JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
    }
}
else {
    JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");
                }
        
    }
    
}
