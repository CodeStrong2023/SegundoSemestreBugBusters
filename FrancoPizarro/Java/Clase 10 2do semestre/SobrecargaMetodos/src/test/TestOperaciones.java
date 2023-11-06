/*
Aca se hacen las pruebas nesecarias para lo que hemos creado en la clase OPERACIONES
 */
package test;

import operaciones.Operaciones;

/**
 *
 * @author Franco
 */
public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = Operaciones.sumar(7, 9); 
        System.out.println("resultado = " + resultado); //Método para sumar enteros
        
        var resultado2 = Operaciones.sumar(5.0, 7);
        System.out.println("resultado2 = " + resultado2); //Método para sumar double
        
        var resultado3 = Operaciones.sumar(8, 6L);
        System.out.println("resultado3 = " + resultado3); //Aunque le pongas un tipo long, el compilador busca
        //un método que sea compatible y que acepte el Long, por eso va a mostrar
        //el método para sumar double
    }
}
