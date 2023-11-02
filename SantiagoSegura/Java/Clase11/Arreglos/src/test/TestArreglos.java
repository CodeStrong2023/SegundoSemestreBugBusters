
package test;

public class TestArreglos {
    public static void main(String[] args) { //Lado derecho instanciamos un objeto de tipo object
        int edades [] = new int [3]; //Del lado izquierdo declaramos la variable
        System.out.println("edades = " + edades);
        
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        edades[1] = 4;
        System.out.println("edades 0 = " + edades [1]);
        
        edades[2] = 28;
        System.out.println("edades 0 = " + edades [2]);
        
        edades[3] = 7; // Fuera de rango, error en tiempo de ejecucion
        
   
        
    }
    
}
