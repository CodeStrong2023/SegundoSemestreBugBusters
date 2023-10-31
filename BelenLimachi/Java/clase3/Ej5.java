package clase3;
import javax.swing.JOptionPane;
public class Ej5 {
    
    public static void main(String[] args) {
       
        int numero,aleatorio, contador =0 ;
        aleatorio = (int)(Math.random()*100);
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
            if(numero < aleatorio){
              JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null, "¡¡Felicidades has acertado el numero!!");
            }
            contador++;
            
        }while(numero !=aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: "+ contador + " intentos");
    }
}
