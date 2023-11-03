
package dominio;

public class Persona {
    private String nombre; //El modificador de acceso private hace que solo se puede acceder 
                           // a estos atributos desde la misma clase, o a traves de metodos 
    private double sueldo;
    private boolean eliminado;
    
    //constructor
    public Persona(String nombre, double sueldo, boolean eliminado) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    //getters y setters

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {//para los booleans, no se usa get, se usa "is"
                                  //Los boolean son como una pregunta, pregunta si esta eliminado
                                  //y retorna true o false
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    //método toString

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", sueldo=" + sueldo 
                + ", eliminado=" + eliminado + '}';
    }
    
}
