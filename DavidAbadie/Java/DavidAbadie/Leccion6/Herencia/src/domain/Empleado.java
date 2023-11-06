
package domain;

public class Empleado extends Persona {
    //Atributos
    private int idEmpleado ;
    private double sueldo;
    private static int contadorEmpleado;
    
    //Constructor   
    public Empleado(){
        idEmpleado = ++Empleado.contadorEmpleado;
    }
        
    public Empleado(String nombre, double sueldo) { //constructor 2
        //super(nombre);
        this(); //Estamos llamando desde aqui al constructor vacio(llamar a un constructor interno)
        this.nombre = nombre;
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
