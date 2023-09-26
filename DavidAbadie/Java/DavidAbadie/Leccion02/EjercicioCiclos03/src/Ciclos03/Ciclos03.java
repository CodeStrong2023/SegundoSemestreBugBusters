/*
Ejercicio 3: Leer números hasta que se introduzzca un cero.
Para cada uno indicar si es par o impar.
Primero se hará con la clase Scanner y luego con las cale JOptionPane
*/
package Ciclos03;

import java.util.Scanner;


public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        int num = entrada.nextInt();
        while(num != 0){ 
            if(num % 2 == 0){
                System.out.println(num +" es PAR");
            }else{
                System.out.println(num +" es IMPAR");
            }
            
            System.out.println("Ingrese un número: ");
            num = entrada.nextInt();
        }
        System.out.println("PROGRAMA FINALIZADO");
    }
}
