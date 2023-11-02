/*

 */
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

/**
 *
 * @author Franco
 */
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Franco", 22000.0); //Los constructores se heredan tambien
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();
        
        Cliente cliente1 = new Cliente(fecha1 , true, "Franco", 'M', 32, "20 de junio 373");
        System.out.println("cliente1 = " + cliente1);
    }
}
