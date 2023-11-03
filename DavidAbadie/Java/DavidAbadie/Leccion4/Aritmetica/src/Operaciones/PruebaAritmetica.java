
package Operaciones;

public class PruebaAritmetica { //solo puede haber una sola clase con el modificador de acceso public
    public static void main(String[] args) {
        int a = 10; //Variables locales
        int b = 7; //Memoria Stack
        
        miMetodo();
        
        //Para almacenar un objeto o los atributos se utiliza la memoria Heap
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
        
        Aritmetica suma4 = new Aritmetica(78, 97); //objeto 4
        System.out.println("suma4 = " + suma4.a);
        System.out.println("suma4 = " + suma4.b);
        
        Persona persona = new Persona("David", "Abadie");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre = " + persona.nombre);
        System.out.println("Persona apellido = " + persona.apellido);
    }
    
    //Otro metodo 
    public static void miMetodo(){
        // a = 10; //El alcance de variables es dentro del mismo metodo.
        //No puedo utilizar una variable que se creó en otro metodo.
        System.out.println("Aqui hay otro metodo");
    }
}

// Crear clases dentro de una misma clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){//Constructor
        super(); //Constructor vacio de la clase Object. Llama a la superclase (clase Object), ya que las demas clases se heredan de 
                //la clase Object. Herencia. 
        new Imprimir().Imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this " + this);//muestra la referencia de memoria del objeto
        //En este caso, "This" hace referencia a sí mismo.
        
       
    }
}

class Imprimir{
    public Imprimir(){
        super();
    }
    
    public void Imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Objeto actual: " + this);
    }
}