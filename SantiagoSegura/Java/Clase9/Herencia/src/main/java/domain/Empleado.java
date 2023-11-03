
package domain;

public class Empleado extends Persona {
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Es para incrementar
    
    //Constructores
    public Empleado(){ //Constructor 1
        this.idEmpleado = ++Empleado.contadorEmpleados;

    }

    public Empleado(String nombre, double sueldo) { //Constructor 2
        //super(nombre);
        this(); //Esramos llamando desde aqui al constructor vacio(llamar al constructor interno)
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
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());

        sb.append('}');
        return sb.toString();
    }
 
}
