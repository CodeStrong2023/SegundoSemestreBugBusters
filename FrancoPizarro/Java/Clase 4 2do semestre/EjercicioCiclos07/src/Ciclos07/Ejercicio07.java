/*
Ejercicio 7: Pedir números hasta que se introduzca uno negativo y calcular la media
 */
package Ciclos07;

import javax.swing.JOptionPane;

/**
 *
 * @author Franco
 */
public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, suma = 0, conteo = 0;
        float promedio;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El número es: "+numero);
            suma += numero;
            conteo++;
             numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }
        if (conteo >= 0){
            JOptionPane.showMessageDialog(null, "ERROR, ha introducido un número negativo, el programa finalizo");
              promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null,"El promedio es "+promedio);
        }
    }
}
