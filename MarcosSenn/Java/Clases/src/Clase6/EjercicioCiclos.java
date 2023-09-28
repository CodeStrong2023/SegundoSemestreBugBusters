package Clase6;
import java.util.Scanner;

//Pedir 10 numeros y calcluar la suma total

public class EjercicioCiclos {
    public static void main(String[] args){
        int acumuladorSuma = 0;
        Scanner pedirNumero = new Scanner(System.in);
        for(int i = 0; i < 10; i++){
            System.out.println("Ingrese un numero");
            int numero = pedirNumero.nextInt();
            acumuladorSuma = acumuladorSuma + numero;
        }
        System.out.println("La suma total es: " + acumuladorSuma);
    }
}
