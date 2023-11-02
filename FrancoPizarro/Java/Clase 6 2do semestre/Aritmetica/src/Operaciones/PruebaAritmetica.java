/*

 */
package Operaciones;

/**
 *
 * @author Franco
 */
public class PruebaAritmetica {
    public static void main(String[] args) {
        
        //Variables locales (tambien se puede utilizar el tipo de inferencia var)
        var a = 10;
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos el método nuevo
        
        Aritmetica aritmetica1 = new Aritmetica(); //La palabra reservada 'new' llama al constructor
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+ resultado);
        
        System.out.println("aritmetica1 a.: "+aritmetica1.a);
        System.out.println("aritmetica2 b.: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8); 
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); = método para limpiar residuos, ES PESADO
    }
    
    public static void miMetodo() {
        int a = 10; //La variable no tiene el alcance por eso se limita y se tiene que llamar
        //este método al método main
        System.out.println("Aqui hay otro método");
    }
}
