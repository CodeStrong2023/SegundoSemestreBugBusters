
package clase3ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio3 {
    public static void main(String[] args) {
        /*
        Ejercicio 3: Realizar un juego para adivbinar un numero, para ello
        generar un numero aleatorio entre 0-100 y luego ir pidiendo numeros indicando
        "es mayor" o "es menor" segun sea mayor o menor con respecto a N.
        El proceso termina cuando el usuario acierta y mostramos el numero de intento hechos. (clase Scanner)
        */
        
        Scanner sc = new Scanner(System.in);
        
        int numAleatorio = (int)Math.round(Math.random()*100); //asignamos el num random que se va a adivinar
        
        System.out.println("Digite un numero: ");
        int num = sc.nextInt();
        int intentos = 0; //contador de intentos
        
        while(num != numAleatorio){
            if(num > numAleatorio){
                System.out.println("Es menor");
                System.out.println("Digite un numero: ");
                num = sc.nextInt();
                intentos++;
            }else{
                System.out.println("Es mayor");
                System.out.println("Digite un numero: ");
                num = sc.nextInt();
                intentos++;
            } 
        }
        System.out.println("Has adivinado en " + intentos + " intentos. El numero era: " + numAleatorio);
        

        
        /*
        Ejercicio 3: Realizar un juego para adivbinar un numero, para ello
        generar un numero aleatorio entre 0-100 y luego ir pidiendo numeros indicando
        "es mayor" o "es menor" segun sea mayor o menor con respecto a N.
        El proceso termina cuando el usuario acierta y mostramos el numero de intento hechos. (clase JOptionPane)
        */
        
        int numAleatorio2 = (int)Math.round(Math.random()*100); //asignamos el num random que se va a adivinar
        int intentos2 = 0; //contador de intentos
        
        int num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        
        while(num2 != numAleatorio2){
            if(num2 > numAleatorio2){
                JOptionPane.showMessageDialog(null, "Es menor");
                num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
                intentos2++;
            }else{
                JOptionPane.showMessageDialog(null, "Es mayor");
                num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
                intentos2++;
            }
        }
         JOptionPane.showMessageDialog(null, "Has adivinado en " + intentos2 + " intentos. El numero era: " + numAleatorio2);
    }
}
