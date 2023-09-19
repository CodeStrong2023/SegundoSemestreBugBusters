
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica suma1 = new Aritmetica(); //objeto 1
        
        suma1.a = 23;
        suma1.b = 7;
        suma1.sumarNumeros(); //no retorna nada
        
        //metodo con retorno del valor
        
        Aritmetica suma2 = new Aritmetica(); //objeto 2
        
        suma2.a = 15;
        suma2.b = 7;
        int resultado = suma2.sumarConRetorno(); //retorna el valor y lo guardo en una variable
        //para poder utilizar el valor que se retorna
        System.out.println("resultado = " + resultado);
        
        //metodo con argumentos
        
        Aritmetica suma3 = new Aritmetica(); //objeto 3
        resultado = suma3.sumarConArgumentos(13, 18);
        System.out.println("Resultado usando argumentos = " + resultado);
    }
}
