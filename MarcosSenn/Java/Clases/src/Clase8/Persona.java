package Clase8;

public class Persona {
    private String nombre;
    private String apellido;
    private int edad;

    public Persona(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public void mostrarDetalles() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
        System.out.println("Edad: " + edad);
    }

    public void modificarDetalles(String nuevoNombre, String nuevoApellido, int nuevaEdad) {
        this.nombre = nuevoNombre;
        this.apellido = nuevoApellido;
        this.edad = nuevaEdad;
    }

    public static void main(String[] args) {
        // Crear el primer objeto de tipo Persona
        Persona persona1 = new Persona("Juan", "Perez", 30);

        // Mostrar detalles iniciales de persona1
        System.out.println("Detalles iniciales de persona1:");
        persona1.mostrarDetalles();

        // Modificar detalles de persona1
        persona1.modificarDetalles("Pedro", "Gomez", 35);

        // Mostrar detalles después de la modificación de persona1
        System.out.println("\nDetalles después de la modificación de persona1:");
        persona1.mostrarDetalles();

        // Crear el segundo objeto de tipo Persona
        Persona persona2 = new Persona("María", "Lopez", 25);

        // Mostrar detalles iniciales de persona2
        System.out.println("\nDetalles iniciales de persona2:");
        persona2.mostrarDetalles();

        // Modificar detalles de persona2
        persona2.modificarDetalles("Laura", "Martinez", 28);

        // Mostrar detalles después de la modificación de persona2
        System.out.println("\nDetalles después de la modificación de persona2:");
        persona2.mostrarDetalles();
    }
}
