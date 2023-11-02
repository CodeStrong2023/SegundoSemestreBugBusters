/*
 */
package test;
//PRUEBAS

import domain.Persona;

/**
 *
 * @author Franco
 */
public class testArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Franco");
        personas[1] = new Persona("Pizarro");
        System.out.println("personas[0] = " + personas[0]);
        System.out.println("personas[1] = " + personas[1]);
        
        for (int i = 0; i < personas.length; i++) {
            System.out.println("personas = "+i+ " = " + personas[i]);
        }
        //trabajamos con arreglos en la sintaxis resumida
        String frutas[] = {"Banana", "pera", "Durazno"};
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("frutas = " + frutas[i]);
            
        }
    }
}
