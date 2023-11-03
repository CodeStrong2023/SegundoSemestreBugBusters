package clase10;

public class Persona {
    public static final String CONSTANTE_AQUI = null;
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    public Persona(){//constructor 1
    }
    public Persona(String nombre){//constructor 2
        this.nombre=nombre;
    }
    public Persona(String nombre,char genero, int edad,String direccion){
        this.nombre=nombre;
        this.genero=genero;
        this.edad=edad;
        this.direccion=direccion;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

    

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    
}
