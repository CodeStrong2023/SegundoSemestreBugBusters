
package clases;

public class Main {
    public static void main(String[] args) {
         Persona persona1 = new Persona(); //Llamamos al constructor
        
        persona1.nombre = "Nicolas";
        persona1.apellido = "Nuñez";
        
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); //Nos muestra la direccion de memoria del objeto
        System.out.println("persona1 = " + persona1);
        
        persona2.obtenerInformacion(); //Al no asignarle un valor, estos tienen el valor null
        
        persona2.nombre = "Saul";
        persona2.apellido = "Hudson";
        persona2.obtenerInformacion();
    }
}
