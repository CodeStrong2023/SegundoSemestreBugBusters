import java.util.Scanner;

public class Ciclos01 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int cuadrado;
        int num = 0;
        while(num >= 0){
            cuadrado = (int)Math.pow(num, 2);
            System.out.println("Ingrese un número positivo: ");
            num = entrada.nextInt();
            if (num >= 0) {
                System.out.println(num + "^2 = " + cuadrado);
            }  
        }
        System.out.println("PROGRAMA FINALIZADO");
    } 
}
