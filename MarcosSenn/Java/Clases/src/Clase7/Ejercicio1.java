package Clase7;
import javax.swing.JOptionPane;
import java.util.ArrayList;

public class Ejercicio1 {
    public static void main(String[] args){
        ArrayList<Integer> array = new ArrayList<>();
        int producto = 1;
        for(int i = 0; i<10;i++){
        String numero = JOptionPane.showInputDialog("Ingrese un numero");
        int num = Integer.parseInt(numero);
        if(num%2!=0){
            array.add(num);
            }
        }
        for(int numero : array){
            producto = producto * numero;
        }
        System.out.println("El producto de los numeros impares es: " + producto);
    }
}
