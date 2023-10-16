
package domain;

public class Empleado extends Persona{
    //Atributos
    private int idEmpleado ;
    private double sueldo;
    private static int contadorEmpleado;
    
    //Constructor   
    public Empleado(String nombre, double sueldo) {
        super(nombre);
        idEmpleado = ++Empleado.contadorEmpleado;
        this.sueldo = sueldo;
    }

    //Getter y Setters
    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    //Clase StringBuilder
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
}
