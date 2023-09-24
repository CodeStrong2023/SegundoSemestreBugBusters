
package Operaciones;

public class Aritmetica {
    
    //Atributos
    int a;
    int b;
    
    //Constructor
    /*
    El constructor:
    1) Construye un objeto
    2) Reserva un espacio en memoria
    3) Inicializa los atributos de la clase
    */
    
    //Constructor por defecto, sin parametros
    public Aritmetica(){ 
        System.out.println("Se esta ejecutando el constructor numero 1");
    }
    
    //sobrecarga de constructores/metodos
    public Aritmetica(int num1, int num2){ //constructor con parametros
        this.a = num1;
        this.b = num2;
        System.out.println("Se esta ejecutando el constructor numero 2");
    }
    
    //Metodos
    public void sumarNumeros(){
        int suma = a + b;
        System.out.println("suma = " + suma);
    }
    
    public int sumarConRetorno(){
        int resultado = a + b; 
        return resultado; // return a + b;
    }
    
    public int sumarConArgumentos(int num1, int b){
        this.a = num1; //no modifica los valores de los atributos del objeto
        this.b = b; //this hace referencia al atributo y no a la variable local
        //this se puede usar cuando el atributo y el argumento tengan el mismo nombre
        
        //return a + b;
        return sumarConRetorno(); //llamamos un metodo dentro de otro metodo
    }
    
    
}
