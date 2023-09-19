package Ciclos03;
import java.util.Scanner;
public class Ciclos03 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0) {
            if(numero % 2 == 0) {
                System.out.println("El numero ingresado "+" es PAR");
            }
            else {
                System.out.println("El numero ingresado "+numero+" es IMPAR");
            }
            numero = Integer.parseInt(entrada.nextLine());
        }  
        System.out.println("El numero ingresado es "+numero+" finaliza el programa");
    }
}
