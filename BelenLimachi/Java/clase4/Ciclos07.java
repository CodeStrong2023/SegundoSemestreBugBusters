package clase4;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(leer.nextLine());
        while (numero >= 0){ //mientras el numero no sea negativo
        suma+= numero;
        conteo ++;
        System.out.println("Digite otra numero");
        numero = Integer.parseInt(leer.nextLine());
        }
        if (conteo ==0){
            System.out.println("\nError la division entre cero no existe = ");
        }
        else {
        promedio = (float)suma/conteo;
            System.out.println("\nEl promedio es: " + promedio);
        }
    }
}
