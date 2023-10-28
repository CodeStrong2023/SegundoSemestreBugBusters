/*

 */
package domain;

/**
 *
 * @author Franco
 */
public class Persona {
    
//atributo
    private String nombre;
    
//constructor
    public Persona(String nombre) {
        this.nombre = nombre;
    }
//getter
    public String getNombre() {
        return nombre;
    }
//setter
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}' + ", " +super.toString();
    }
    
    
}
