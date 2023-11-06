package clase9;
import clase9.Cliente;
import clase9.Empleado;
import java.util.Date;

public class PruebaHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Belen", 120000.00);
        System.out.println("empleado1 = " + empleado1);
        Date fecha1 = new Date();
        Cliente cliente1 = new Cliente(fecha1, true, "Jorge",'M', 25, "SinNumero");
        System.out.println("cliente1 = " + cliente1);
        }
}
