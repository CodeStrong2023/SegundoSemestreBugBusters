/*

 */
package Operaciones;

/**
 *
 * @author Franco
 */
//CLASE MAIN DONDE SE LLAMAN LOS METODOS
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
        
        Persona persona = new Persona("Franco", "Pizarro");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona nombre: "+persona.apellido);
    }
    //Modularidad creamos un nuevo método
    public static void miMetodo() {
        int a = 10; //La variable no tiene el alcance por eso se limita y se tiene que llamar
        //este método al método main
        System.out.println("Aqui hay otro método");
    }
}
//Craamos una nueva clase dentro de otra
class Persona{ //Se le asigna un tipo default o package que se crea automaticamente
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
//        super(); //llamada al constructor de la clase Padre object
//        Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido; 
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}