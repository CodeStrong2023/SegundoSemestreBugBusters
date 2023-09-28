
package pasoporvalor;

public class PasoPorValor {
    public static void main(String[] args) {
        int valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); //Solo le enviamos una copia
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){ //recibe una copia del valor de la variable, 
        //no modifica el espacio de memoria de la variable local
        //No puede manipular el valor de la variable, porque solo recibió una copia 
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }
}
