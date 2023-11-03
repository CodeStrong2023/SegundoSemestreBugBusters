/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo y a continuacion
realizar la media de los números positivos,la media de los negativos y contar el número
de ceros
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

/**
 *
 * @author Franco
 */
public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        float positivos=0, negativos=0, mediaPositivos, mediaNegativos;
        int conteo0 = 0, conteoPositivos = 0, conteoNegativos = 0;
        
        float[] numeros = new float[5];
        System.out.println("Escriba los valores del arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.print((i+1)+ ". Digite el valor para el arreglo: ");
            numeros[i] = entrada.nextFloat();
            
            if (numeros[i] == 0){
                conteo0++;
            }   
            else if(numeros[i] > 0){
            positivos += numeros[i];
            conteoPositivos++;
            }
            else{
                negativos += numeros[i];
                conteoNegativos++;
            }
        }
        
        //Media de los números positivos
        if (conteoPositivos == 0){
            System.out.println("No se puede sacar la media de los números positivos");
        }
        else{
            mediaPositivos = positivos / conteoPositivos;
            System.out.println("La media de los números positivos es: "+ mediaPositivos);
        }
        
        //Media de los números negativos
        if(conteoNegativos == 0){
            System.out.println("No se puede sacar la media de los números negativos");
        }
        else{
            mediaNegativos = negativos / conteoNegativos;
            System.out.println("La media de los números negativos son: " +mediaNegativos);
        }
        
        System.out.println("La cantidad de ceros es: "+ conteo0);
    }
}
