
package Operaciones;

public class Aritmetica {
    
    //Atributos
    int a;
    int b;
    
    //Metodos
    public void sumarNumeros(){
        int suma = a + b;
        System.out.println("suma = " + suma);
    }
    
    public int sumarConRetorno(){
        int resultado = a + b; 
        return resultado; // return a + b;
    }
    
    public int sumarConArgumentos(int num1, int num2){
        a = num1; //no modifica los valores de los atributos del objeto
        b = num2;
        //return a + b;
        return sumarConRetorno(); //llamamos un metodo dentro de otro metodo
    }
    
    
}
