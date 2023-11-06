package Clase9;

public class Empleado {
    private int idEmpleado;
    private String nombre;
    private double sueldo;

    public Empleado(String nombre, double sueldo) {
        super();
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado { idEmpleado=").append(idEmpleado);
        sb.append(", nombre=").append(nombre);
        sb.append(", sueldo=").append(sueldo);
        sb.append(" }");
        return sb.toString();
    }
}
