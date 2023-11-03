/*
 */
package domain;

/**
 *
 * @author Franco
 */
public class Persona {
    // si le ponemos el 'final' creamos una clase ctte
    
    //atributo
    public final static int CONSTANTE_AQUI = 15;

    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
    public final void imprimir(){
        System.out.println("Método para imprimir");
    }
}
