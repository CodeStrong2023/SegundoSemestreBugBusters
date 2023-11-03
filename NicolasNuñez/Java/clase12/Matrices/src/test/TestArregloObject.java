
package test;

import domain.Persona;

public class TestArregloObject {
    public static void main(String[] args) {
        
        Persona personas[] = new Persona[3];
        personas[0] = new Persona("Nicolas");
        personas[1] = new Persona("Ariel");
        personas[2] = new Persona("Osvaldo");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        System.out.println("personas 2 = " + personas[2]);
        
        System.out.println(" ");
        
        for(int i = 0; i < personas.length; i++){
            System.out.println("Personas " + i + " = " + personas[i]);
        }
        
        System.out.println(" ");
        
        //Sintaxis resumida
        String frutas[] = {"Banana", "Pera", "Naranja", "Durazno"};
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("Frutas: " + frutas[i]);
        }
    }
}
