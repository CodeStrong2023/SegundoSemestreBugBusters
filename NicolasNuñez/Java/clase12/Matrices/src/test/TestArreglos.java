
package test;


public class TestArreglos {
    public static void main(String[] args) {
        
        int edades[] = new int[3]; //los arrays son de tipo object. Heredan de la clase object
        //No se puede modificar la cantidad de elementos del array. 
        System.out.println("edades = " + edades);
        
        edades[0] = 21;
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 50;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 18;
        System.out.println("edades 2 = " + edades[2]);
        
        //edades[3] = 7 //Fuera de rango, error en tiempo de ejecución
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("Edad " + i + ": " + edades[i]);
        }
    }
}
