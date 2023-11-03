package Clase6;

public class PruebaCaja {
    public static void main(String[] args) {
        Caja caja1 = new Caja(3, 2, 6);
        Caja caja2 = new Caja(4, 5, 2);
        System.out.println("El volumen de la caja 1 es: " + caja1.CalcularVolumen());
        System.out.println("El volumen de la caja 2 es: " + caja2.CalcularVolumen());
    }
}

