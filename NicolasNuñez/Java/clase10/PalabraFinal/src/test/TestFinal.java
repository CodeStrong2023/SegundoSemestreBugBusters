/*
Uso de la palabra Final:
Esta palabra tiene diferentes significados dependiendo de donde se aplique:
    variables: Evitar cambiar el valor que almacena la variable (constante).
    métodos: Evita que se modifique la definicion de un método desde una subclase.
    clases: Evita que se creen clases hijas.

Otra caracteristicas es que normalmente, cuando trabajamos con variables se combina con el modificador de acceso
estatico para convertir una variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cual todos sus atributos son de tipo static y final, es por esto
que la variable pi se conoce como una constante.
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDNI = 44248194;
        System.out.println("miDNI = " + miDNI);
        
        //miDNI = 12345678; //No se puede cambiar el valor de una constante. 
        
        //Persona.CONSTANTE_AQUI = 9; No se modifica
        System.out.println("Mi atributo constante es " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede agregar una nueva referencia
        
        persona1.setNombre("Nicolas");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Ariel");
        System.out.println("persona1 nombre = " + persona1.getNombre());
    }
}
