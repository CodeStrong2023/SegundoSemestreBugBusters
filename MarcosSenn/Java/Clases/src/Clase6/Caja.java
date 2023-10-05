package Clase6;

public class Caja {
    int alto;
    int ancho;
    int profundidad;

    public Caja() {
    }

    public Caja(int alto,int ancho,int profundidad){
        this.alto = alto;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }

    int CalcularVolumen(){
        return alto * ancho * profundidad;
    }
}
