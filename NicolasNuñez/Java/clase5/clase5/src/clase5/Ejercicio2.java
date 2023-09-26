package clase5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio2 {

    public static void main(String[] args) {
        /*
        Ejercicio 2: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
        Suponiendo que todos los meses son de 30 dias. (Clase Scanner)
         */

        Scanner sc = new Scanner(System.in);
        
        int dia, mes, year;
        
        System.out.println("Digite un dia: ");
        dia = sc.nextInt();
        
        System.out.println("Digite un mes: ");
        mes = sc.nextInt();
        
        System.out.println("Digite un anio: ");
        year = sc.nextInt();
        
        if((dia != 0) && (dia <= 30)){
            if((mes != 0) && (mes <= 12)){
                if((year != 0) && (year <= 2023)){
                    System.out.println("La fecha ingresa es: " + dia + "/" + mes + "/" + year);
                    System.out.println("La fecha ingresada es correcta");
                }else{
                    System.out.println("Fecha incorrecta. Año incorrecto");
                }
            }else{
                System.out.println("Fecha incorrecta. Mes incorrecto");
            }
        }else{
            System.out.println("Fecha incorrecta. Dia incorrecto");
        }
         
        /*
        Ejercicio 2: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
        Suponiendo que todos los meses son de 30 dias. (Clase JOptionPane)
         */
        
        int dia1 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un dia: "));

        int mes2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un anio: "));

        if((dia1 != 0) && (dia1 <= 30)) {
            if((mes2 != 0) && (mes2 <= 12)) {
                if((anio != 0) && (anio <= 2023)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresa es: " + dia1 + "/" + mes2 + "/" + anio);
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es correcta");
                }else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta. Año incorrecto");
                }
            }else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta. Mes incorrecto");
            }
        }else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta. Dia incorrecto");

        }
    }
}
