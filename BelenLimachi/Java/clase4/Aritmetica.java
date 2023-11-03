package clase4;


public class Aritmetica {
    //Atributos de la clase
    int a;  
    int b;
    
    //El constructo es un metodo especial (tiene 3 objetivos: 
        // 1-construye un objeto 
        // 2- Reserva un espacio en memoria
        //3- Incializa los atributos de la clase
    
    public Aritmetica(){ //Constructor 1 vacio
        System.out.println("Se esta ejecutando el constructor n°1 ");
    }
    
    //estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a , int b){//constructor 2
    this.a= a;
    this.b= b;
        System.out.println("Se esta ejecutando el constructor n°2");
    }
    
    
    
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    //otro metodo
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento "a" se asigna al atriburo "this.a"
        this.b = b;
        //return a+b;
        return this.sumarConRetorno();
    }
}