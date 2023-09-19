/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y luego ir pidiendo
números indicando "es mayor" o "es menor" según sea mayor o menor
con respecto a N.
El proceso termina cuando el usuario acierta y mostramos el número
de intentos hechos.
*/
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        int num, aleatorio, contador = 0;
        aleatorio = (int)(Math.random()*100); // Genera un numero aleatorio
        
        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Adivine el número: "));
            if(num > aleatorio){
                JOptionPane.showMessageDialog(null, "Ingrese un número menor");
            }else if(num < aleatorio){
                JOptionPane.showMessageDialog(null, "Ingrese un número mayor");
            }else{
                JOptionPane.showMessageDialog(null, "¡¡¡FELICIDADES!!! Has adivinado el número :)");
            }
            contador++;
        }while(num != aleatorio);   
        JOptionPane.showMessageDialog(null, "Adivinaste el número en: "+contador+" intentos");
    }
}
