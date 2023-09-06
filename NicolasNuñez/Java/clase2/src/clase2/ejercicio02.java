package clase2;

import javax.swing.JOptionPane;

public class ejercicio02 {

    public static void main(String[] args) {
        //Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir
        //el proceso hasta que se introduzca un numero negativo (JOptionPane)

        int num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        while (num >= 0) {
            int numCuadrado = (int)Math.pow(num,2);
            JOptionPane.showMessageDialog(null, "El numero " + num + " elevado al cuadrado es: " + numCuadrado );
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        JOptionPane.showMessageDialog(null, "El prgrama ha finalizado por numero negativo");
    }
}
