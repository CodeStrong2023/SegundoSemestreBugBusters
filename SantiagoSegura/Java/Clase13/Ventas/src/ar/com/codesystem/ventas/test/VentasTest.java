
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 12500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Zapatos", 66000.00);
        Producto producto4 = new Producto("Remera", 8500.00);
        Producto producto5 = new Producto("Buzo", 20000.00);
        Producto producto6 = new Producto("Lentes", 6800.00);


        
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();

        
        //Agregamos productos a la lista
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden2.agregarProducto(producto3); // Nuevos productos
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5); 
        orden2.agregarProducto(producto6);
        orden1.mostrarOrden();
        orden2.mostrarOrden();

        
        
        //Tarea:
        //Crear más objetos de tipo Producto 
        //Crear mas objetos de tipo Orden
        

    }
    
}
