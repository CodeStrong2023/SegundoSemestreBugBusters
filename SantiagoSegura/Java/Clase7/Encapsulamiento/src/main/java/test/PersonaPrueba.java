
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Santiago", 57.000, false); 
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        // persona1.nombre = "Juan Ignacio"; // Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        System.out.println("persona1: "+persona1.toString());
        //Tarea: Crear otr objeto de tipo persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
    }
    
    
    public class Persona {
    String nombre;
    String apellido;
    int edad;

    public Persona(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }
        Persona persona1 = new Persona("Juan", "Zalazar", 22);

        System.out.println("Valores iniciales:");
        System.out.println("Nombre: " + persona1.nombre);
        System.out.println("Apellido: " + persona1.apellido);
        System.out.println("Edad: " + persona1.edad);

        persona1.nombre = "María";
        persona1.edad = 25;

        System.out.println("\nValores modificados:");
        System.out.println("Nombre: " + persona1.nombre);
        System.out.println("Apellido: " + persona1.apellido);
        System.out.println("Edad: " + persona1.edad);
    }
    
    
    
}

    
         
