/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
    variables: evita cambiar el valor que almacena la variable
    métodos: evita que se modifique la definicion o el comportamiento
             de un método desde una subclase (hija)
    clase: evita que se creen nuevas clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables se combina
con el modificador de acceso estático para convertir una variable en una constante, es decir
que no se puede modificar su valor, el ejemplo de esto es la clase Math en la cuál
todos sus atrubutos son de tipo static y final, es por esto que la variable pi* se conoce
como una constante.
 */
package test;

import domain.Persona;

/**
 *
 * @author Franco
 */
public class TestFinal {
    public static void main(String[] args) {
        final int miDNI = 434524252;
        System.out.println("miDNI = " + miDNI);
//      Persona.CONSTANTE_AQUI = 9; //no se modifica
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        // persona1 = new Persona(); // No se puede asignar una nueva referencia
        persona1.setNombre("Franco Pizarro");
        System.out.println("persona1 nombre: " + persona1.getNombre());
        // no se puede modificar la referencia pero si el contenido de la variable
        persona1.setNombre("Sebastian");
        System.out.println("persona1 nombre: " + persona1.getNombre());
    }
}
