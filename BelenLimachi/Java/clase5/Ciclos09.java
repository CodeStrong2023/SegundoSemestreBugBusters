package clase5;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Digite el dia: ");
        int dia = Integer.parseInt(leer.nextLine());
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(leer.nextLine());
        System.out.println("Digite el año: ");
        int anio = Integer.parseInt(leer.nextLine());
        
        if ((dia != 0) &&(dia <= 30) ){
            if ((mes !=0) && (mes <=12)){
                if ((anio !=0)&& (anio <=2023)){
                    System.out.println("La fecha ingresada es: " +dia+ "/" + mes+ "/" + anio );
                }
                else {
                    System.out.println("Fecha incorrecta , año incorrecto ");
                }
            }
            else {
                System.out.println("Fecha incorrecta , mes incorrecto ");
            }
        }
        else {
            System.out.println("Fecha incorrecta, dia incorrecto ");
        }
            
    }
}
