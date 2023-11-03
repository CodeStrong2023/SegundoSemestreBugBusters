/*
Ejercicio 5: Realizar un juego para adivinar un número, para ello generar un nuúmero aleatorio
entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" 
según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos
 */
package Ciclos05;

import javax.swing.JOptionPane;



/**
 *
 * @author Franco
 */
public class Ejercicio05 {
    public static void main(String[] args) {
        
        int numero, numAleatorio, conteo = 0;
        JOptionPane.showMessageDialog(null,"VAMOS A JUGAR");
        JOptionPane.showMessageDialog(null,"***El número aleatorio se ha generado***");
        numAleatorio = (int)(Math.random()*100); //Esto genera un númeo aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
            if(numero < numAleatorio){
                JOptionPane.showMessageDialog(null,"Digite un número MAYOR");
            }
            else if(numero > numAleatorio){
                JOptionPane.showMessageDialog(null,"Digite un número MENOR");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡FELICIDADES! Haz encontrado el número");
                JOptionPane.showMessageDialog(null, "El numero aleatorio era "+numero);
            }
            conteo++;
        }while(numero != numAleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el número en: "+conteo+" intentos");
    }
}

