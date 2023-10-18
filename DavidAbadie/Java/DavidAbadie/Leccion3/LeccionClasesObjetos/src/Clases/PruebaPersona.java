
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "David"; //El valor hexadecimal normalmente comienza con 0x (ref. a memoria)
        persona1.apellido = "Abadie";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}
