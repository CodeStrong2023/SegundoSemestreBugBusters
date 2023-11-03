/*
Proyecto caja:
Eejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuacion
La formula es: volumen = ancho * alto * profundidad
*/

package caja;

public class PruebaCaja {
    public static void main(String[] args) { //Metodo main
        //Variables locales
        int medidaAncho = 3; //Valores ingresados en codigo duro
        int mediaAlto = 2;
        int mediaProf = 6;
        
        Caja caja1 = new Caja (); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = mediaAlto;
        caja1.profundo = mediaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al metodo
        //Primer resultado
        System.out.println("resultado volumen de la caja 1:" +resultado);
        
        Caja caja2 = new Caja(2, 5, 6); // Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el al metodo para un nuevo calculo
        System.out.println("resultado volumen de caja 2:" + caja2.calcularVolumen());
        
        
    }
    
}
