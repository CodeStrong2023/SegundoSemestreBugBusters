import java.util.Scanner;

//Ejercicio2: Leer un numero e indicar si es positivo o negativo. El proceso se repite hasta que se introduzca un 0
public class Ejercicio02 {
    public static void main(String[] args){

        while(true){
            Scanner scanner = new Scanner((System.in));

            System.out.println("Ingrese un numero o cero para finalizar");

            int numero = scanner.nextInt();

            if(numero==0){
                System.out.println("Programa finalizado");
                break;}
            else if(numero>0){
                System.out.println("Se ingreso un numero positivo");
            }

            else {
                System.out.println("Se ingreso un numero negativo");
            }

        }
    }
}
