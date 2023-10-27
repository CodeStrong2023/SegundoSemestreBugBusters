
package domain;

/**
 *
 * @author Franco
 */
public class Empleado extends Persona{
    //Clase padre es Persona y esta clase es la hija,
    //para hacerlo debemos poner 'extends' y el nombre de la clase padre
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //es para incrementar
    
    //constructor
    public Empleado(String nombre, double sueldo) {
        super(nombre);
        this.idEmpleado = ++Empleado.contadorEmpleados;
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

    /*
    El StringBuilder es una clase que es mas eficiente que el metodo toString común
    el singo '+' es mas lento para concatenar objetos tipo str o cadenas. Por lo que
    el StringBuilder es mas rapido, tambien con el método append se agregan los atributos
    Al finalizar va a utilizar la variable 'sb' creada desde la clase StringBuilder
    pero no es compatible con el retorno por lo que se pone el objeto.toString que debe ser
    compatible con el método toString
    */
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
