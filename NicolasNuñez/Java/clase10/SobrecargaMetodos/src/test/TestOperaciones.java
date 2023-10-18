
package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        int resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        double resultado2 = Operaciones.sumar(23.265, 12.54);
        System.out.println("resultado2 = " + resultado2);
        
        var resultado3 = Operaciones.sumar(6, 8L);
        System.out.println("resultado3 = " + resultado3);
    }
}
