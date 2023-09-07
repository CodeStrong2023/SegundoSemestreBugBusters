/*
Realizar un juego para adivinar un numero, para ello
generar un numero aleatorio entre 0-100 y luego ir 
pidiendo numeros indicando "es mayor" o "es menor"
segun sea mayor o menor con respecto a N 
El proceso termina cuando el usuario acerta y 
mostramos el numero de intentos hechos.
*/
package Ciclos05;
import javax.swing.JOptionPane;
public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //Est genera un numero aleatorio
        do{ 
            numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un numero: "));
            if(numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            }
            else {
                JOptionPane.showMessageDialog(null, "Felicidades! Advinaste el numero :3!");
            }
            conteo++;
        }while(numero !=aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en "+conteo+" intentos");
    } 
}
