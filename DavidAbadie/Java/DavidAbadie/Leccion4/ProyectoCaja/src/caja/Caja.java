package caja;
 // Proyecto caja
    /*
    Ejercicio 1: Crear un proyecto segun las especificaciones mostradas a continuacion: 
    La formula es: volumen = ancho * alto * profundidad
    */

public class Caja { //Clase publica caja
    //Atributos
    public double ancho;
    public double alto;
    public double profundidad;
    
    //Constructores
    
    //constructor vacio
    public Caja(){
        this(20.25, 40.6, 60.1);
        
    }

    //constructor con parametros
    public Caja(double ancho, double alto, double profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    //Metodos personalizados
    
    public void mostarVolumen(){
        double volumen = ancho * alto * profundidad;
        System.out.println("El volumen de la caja es de: " + volumen + " centimetros cubicos cm3");
    }
}

