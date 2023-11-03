package clase7.Encapsulamiento;

public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.eliminado = eliminado;
        this.sueldo = sueldo;
    }
    //metodos set y get (lo abrimos con click derechos sobre la linea/insert code/elegimos

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

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    public String toString(){//Convierte en una cadena cada atributo
        return "Pesona [ nombre: "+ this.nombre +
                ", sueldo: "+ this.sueldo+
                ", eliminado: " + this.eliminado+ "]";
    }
}
