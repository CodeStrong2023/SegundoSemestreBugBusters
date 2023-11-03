/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 dias.
*/
package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Dia: ");
        int dia = scanner.nextInt();
        System.out.println("Mes: ");
        int mes = scanner.nextInt();
        System.out.println("Año: ");
        int anio = scanner.nextInt();
        if((dia != 0)&&(dia <= 30)){
            if((mes != 0)&&(mes <= 12)){
                if((anio != 0)&&(anio <= 2023)){
                    System.out.println("La fecha es: "+dia+"/"+mes+"/"+anio);
                }else{
                    System.out.println("Fecha incorrecta, año incorrecto");
                }
            }else{
                System.out.println("Fecha incorrecta, mes incorrecto");
            }
        }else{
            System.out.println("Fecha incorrecta, dia incorrecto");
        }
    }
}
