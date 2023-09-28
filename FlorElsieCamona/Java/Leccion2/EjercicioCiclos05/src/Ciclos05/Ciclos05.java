package Ciclos05;
import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //Est genera un numero aleatorio
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio) {
                System.out.println("Digite un numero mayor");
            }
            else if(numero > aleatorio) {
                System.out.println("Digite un numero menor");
            }
            else {
                System.out.println("Felicidades! Adivinaste el numero!! :3!");
            }
            conteo++;
        }while(numero !=aleatorio);
        System.out.println("Adiviniste el numero en: "+conteo+" intentos");
    }       
}
