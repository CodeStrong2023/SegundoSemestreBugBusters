/*

 */
package test;

import dominio.Persona;
/**
 *
 * @author Franco
 */
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Franco", 22.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
        //modificar a través de los métodos
        persona1.setNombre("Juan Cruz");
//        persona1.nombre = "Juan Cruz"; Ya no se puede utilizar
//        System.out.println("Nombre es: "+persona1.nombre);
//      Imprimimos los resultados
        System.out.println("persona1 con su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
//TAREA: crear otro objeto de tipo persona, asignar valores de manera inicial y imprimir
//lugo modificar sus valores y volver a imprimir

        System.out.println("persona1 = " + persona1.toString());

    }
}
