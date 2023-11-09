
package test;

import domain.Persona;

/**
 *
 * @author Franco
 */
public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5; //Llenado manual
        edades[0][1] = 7; //Es una diferente columna
        edades[1][0] = 8; 
        edades[1][1] = 4; 
        edades[2][0] = 10;
        edades[2][1]  = 11;
        
        System.out.println("Edades 0-0 = " + edades[0][0]);
        System.out.println("Edades 0-1 = " + edades[0][1]);
        System.out.println("Edades 1-0 = " + edades[1][0]);
        System.out.println("Edades 1-1 = " + edades[1][1]);
        System.out.println("Edades 2-0 = " + edades[2][0]);
        System.out.println("Edades 2-1 = " + edades[2][1]);
        
        System.out.println("Recorremos la matriz a través del ciclo for");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("edades " + fila +"-"+ col +": "+edades[fila][col]);
            }   
        }
        System.out.println("Matriz Frutas");
        // Sintaxis clasica
        //String frutas[][] = new String [3][2];
        
        //SINTAXIS SIMPLIFICADA
        String frutas[][] = {{"Limon", "pomelo"},{"Ciruela", "kiwi"},{"Banana", "Manzana"}};
        imprimir(frutas);
//        for (int i = 0; i < frutas.length; i++) {
//                for (int j = 0; j < frutas[i].length; j++) {
//                    System.out.println("frutas " + i +"-"+ j +": "+frutas[i][j]);
//                }
//        }
        
        //Creamos una matriz de objetos
        Persona personas[][] = new Persona[2][3];
        
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Ariel");
        personas[0][1] = new Persona("Osvaldo");
        personas[0][2] = new Persona("Natalia");
        personas[1][0] = new Persona("Franco");
        personas[1][1] = new Persona("Juan Cruz");
        personas[1][2] = new Persona("Sebastian");
        System.out.println("Matriz de Personas");
        imprimir(personas);
    }
    
    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
                for (int j = 0; j < matriz[i].length; j++) {
                    System.out.println("frutas " + i +"-"+ j +": "+matriz[i][j]);
                }
        }
    }
}
