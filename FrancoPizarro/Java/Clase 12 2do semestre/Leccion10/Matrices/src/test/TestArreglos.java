/*

 */
package test;

/**
 *
 * @author Franco
 */
public class TestArreglos {
    public static void main(String[] args) {
        int edades [] = new int [3]; //se utiliza la palabra new pq son un tipo object
/* en el lado izquierdo declaramos la variable, y en la lado derecho instanciamos un objeto de tipo object*/
// Al indicar el cantidad de elementos [3] ya no se puede cambiar de forma dinamica
        System.out.println("edades = " + edades);
        
        edades[0] = 20; // Le asignamos un valor al espacio 0 del arreglo
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 22; // Le asignamos un valos al espacio 1 del arreglo
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 11; // Le asignamos un valos al espacio 2 del arreglo
        System.out.println("edades [2] = " + edades[2]);
//        edades[3] = 2003; // Le asignamos un valos al espacio 3 del arreglo
//        System.out.println("edades [3] = " + edades [3]); //Fuera de rango, erros en tiempo de ejecucion

        for (int i = 0; i < edades.length; i++) { //length es la longitud del arreglo
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
    }
}
