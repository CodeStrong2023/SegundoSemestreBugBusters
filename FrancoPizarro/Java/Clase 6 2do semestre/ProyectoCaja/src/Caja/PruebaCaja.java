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
public class PruebaCaja {
    public static void main(String[] args) { //Método main
        //Variables locales, valores ingresados en código duro
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();//Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen();
        
        //Primer resultado
        System.out.println("resultado volumen de caja 1: " + resultado);
        
        Caja caja2 = new Caja(2, 4, 6); //Llamamos al constructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo calculo
        System.out.println("Resultado de volumen de la caja 2: " + caja2.calcularVolumen());
    }
}
