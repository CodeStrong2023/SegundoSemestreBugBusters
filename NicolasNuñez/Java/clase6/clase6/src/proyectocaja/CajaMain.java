
package proyectocaja;


public class CajaMain {
    public static void main(String[] args) {
        Caja caja1 = new Caja(); //Objeto 1 - constructor vacio
        
        caja1.ancho = 55;
        caja1.alto = 40;
        caja1.profundidad = 30;
        System.out.println("Caja 1: ");
        caja1.mostarVolumen();
        
        Caja caja2 = new Caja(20.55, 40.12, 60.50); //Objeto 2 - constructor con parametros
        
        System.out.println("Caja 2: ");
        caja2.mostarVolumen();
        
                
    }
}
