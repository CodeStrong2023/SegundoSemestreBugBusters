
package ar.com.codesystem.ventas;

public class Orden {
    //Atributos
    private int idOrden;
    private Producto productos[]; //Declaramos el vector
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;

    //Constructor vacio
    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    //Métodos
    public void agregarProducto(Producto producto){
        if(contadorProductos < MAX_PRODUCTOS){
            productos[contadorProductos++] = producto;
        }else{
            System.out.println("Se ha superado el maximo de productos: " + MAX_PRODUCTOS);
        }
    }
    
    public double calcularTotal(){
        double total = 0;
        for(int i = 0; i < contadorProductos; i++){
//            Producto producto = productos[i];
//            total += producto.getPrecio();
            total += productos[i].getPrecio();
        }
        return total;
    }
    
    public void mostrarOrden(){
        System.out.println("Id Orden: " + idOrden);
        double totalOrden = calcularTotal();
        System.out.println("El total de la orden es: $" + totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < contadorProductos; i++) {
            System.out.println(productos[i]);
        }
    }
}
