
package test;

import dominio.Persona;
// import dominio.*; --> importa todas las clases del paquete dominio
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println(persona1);
        System.out.println("Persona1 nombre = " + persona1.getNombre());
        //Modificar a través de los métodos
        persona1.setNombre("Nicolas");
        //persona1.nombre = "Nicolas"; //no se puede modificar porque el atributo es privado
        System.out.println("Persona1 con su nombre modificado = " + persona1.getNombre());
        System.out.println("persona1 sueldo = " + persona1.getSueldo());
        System.out.println("persona1 booleano = " + persona1.isEliminado());
        
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial 
        //e imprimir, luego modificar sus valores y volver a imprimir.
        
        System.out.println("\n");
        
        Persona persona2 = new Persona("Ariel", 132000.45, true);
        System.out.println("Persona2 nombre = " + persona2.getNombre());
        System.out.println("persona2 sueldo = " + persona2.getSueldo());
        System.out.println("persona2 booleano = " + persona2.isEliminado());
        
        //modificamos los valores
        persona2.setNombre("Natalia");
        persona2.setSueldo(145550.13);
        persona2.setEliminado(false);
        
        System.out.println("Persona2 con su nombre modificado = " + persona2.getNombre());
        System.out.println("persona2 con su sueldo modificado = " + persona2.getSueldo());
        System.out.println("persona2 con su booleano modificado = " + persona2.isEliminado());
        
        
        System.out.println(persona2); //utilizando el metodo toString
        
        
    }
}
