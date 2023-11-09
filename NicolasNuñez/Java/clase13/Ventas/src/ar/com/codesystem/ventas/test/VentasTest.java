
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;


public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //TAREA:
        //Crear objetos de tipo Producto: 10
        //Crear objetos de tipo Orden: 2
    }
}
