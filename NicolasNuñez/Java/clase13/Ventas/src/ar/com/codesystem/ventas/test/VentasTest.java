
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
        
        System.out.println(" ");
        Orden orden2 = new Orden();
        Producto producto3 = new Producto("Remera", 6290.00);
        Producto producto4 = new Producto("Camisa", 7899.55);
        Producto producto5 = new Producto("Zapatillas", 32470.93);
        Producto producto6 = new Producto("Cinturon", 4200.00);
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.mostrarOrden();
        
        System.out.println(" ");
        Orden orden3 = new Orden();
        Producto producto7 = new Producto("Medias", 1760.00);
        Producto producto8 = new Producto("Boxer", 2990.50);
        Producto producto9 = new Producto("Gorra", 14200.00);
        Producto producto10 = new Producto("Vestido", 18950.15);
        Producto producto11 = new Producto("Buzo", 21300.55);
        Producto producto12 = new Producto("Perfume", 8180.65);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        orden3.mostrarOrden();
    }
}
