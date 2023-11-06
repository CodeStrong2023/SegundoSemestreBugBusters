/*
Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo
que todos los meses son de 30 días.
 */
package Ciclos09;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int dia, mes, año;
        System.out.println("Digite un día: ");
        dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite un mes: ");
        mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite un año: ");
        año = Integer.parseInt(entrada.nextLine());
        if ((dia != 0) && (dia <= 30)){
            if ((mes != 0) && (mes <= 12)){
                if ((año != 0) && (año <= 2022)){
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+año);
                }
                else{
                    System.out.println("Fecha incorrecta, año incorrecto");
                }
            }
            else{
                System.out.println("Fecha incorrecta, mes incorrecto");
            }
        }
        else{
            System.out.println("Fecha incorrecto, día incorrecto");
        }
    }
}