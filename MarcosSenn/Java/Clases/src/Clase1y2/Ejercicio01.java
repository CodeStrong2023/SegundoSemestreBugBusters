package Clase1y2;
import java.util.Scanner;

public class Ejercicio01 {
    public static void main(String[] args) {
        while (true){
            Scanner ingresoDatos = new Scanner((System.in));
            System.out.println("ingrese un numero para calcular su cadrado");
            int numero = ingresoDatos.nextInt();
            if(numero<0){
                System.out.println("Programa finalizado");
                break;}
            else{
                int cuadrado = numero*numero;
                System.out.println(cuadrado);
            }
        }

    }
}