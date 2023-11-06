
package test;

import domain.Persona;

public class TestArreglosObjetc {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Santiago");
        personas[1] = new Persona("Ariel");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        
        for(int i = 0; i < personas.lenght; i ++){
            System.out.println("personas = "+i+" = " + personas[1]);
        }
        //Trabajamos con arreglos en la sintaxis resumida
        String frutas[] = {"Banana", "Manzana", "Pera"};
        for(int i = 0; i < furtas.lenght; i++){
            System.out.println("frutas " +i+" = "+ frutas[i]);
        }

    }
    
}
