
package test;
import domain.Persona;

public class PersonaPrueba {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Ariel");
        System.out.println("persona1 = " + persona1);
        
        Persona persona2 = new Persona("David");
        System.out.println("persona2 = " + persona2);
        
        Persona persona3 = new Persona("Natalia");
        System.out.println("persona3 = " + persona3);
        
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10; //No se puede referenciar una atributo dinamico desde un contexto estático
        
       PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return contador;
    }
}
