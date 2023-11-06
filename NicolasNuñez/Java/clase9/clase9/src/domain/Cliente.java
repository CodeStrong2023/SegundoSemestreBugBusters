
package domain;
import java.util.Date;

public class Cliente extends Persona{
    //Atributos
    private static int idCliente;
    private Date fechaRegistro;
    private boolean vip;
    
    //constructor

    public Cliente(String nombre, char genero, int edad, String direccion, Date fechaRegistro, boolean vip) {
        super(nombre,genero,edad,direccion);
        idCliente++;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }
   
    //Getters y Setters

    public int getIdCliente() {
        return idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }
    
    public boolean isVip() { //getter
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
}
