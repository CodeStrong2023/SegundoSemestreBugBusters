/*
Proyecto caja:
Ejercicio 1: crear un proyecto según las especificaciones mostradaas a continuacion.
La formula es: volumen = ancho * alto * profundidad
 */
package Caja;

/**
 *
 * @author Franco
 */
public class Caja { //Clase publica Caja
    
    //Atributos (Caracteristas)
    int ancho;
    int alto;
    int profundidad;
    
    //Métodos y constructores (acciones)
    public Caja (){
        //Constructor vacio
    }
   public Caja(int ancho, int alto, int profundidad){ //Constructor 2
       this.ancho = ancho;
       this.alto = alto;
       this.profundidad = profundidad;
   }
   
   public int calcularVolumen(){ //Método para calcular
       return ancho * alto * profundidad;
   }
}
