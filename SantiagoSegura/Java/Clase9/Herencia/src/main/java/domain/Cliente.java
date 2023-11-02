
package domain;

import java.util.Date;

public class Cliente extends Persona {
    //Atributos
    private int idCliente;
    private Date fechaRegistro; //Importar la clase Date
    private boolean vip; //Very important person
    private static int contadorCliente; //Tipo estatico
    
    //Constructor
   public Cliente(Date fechaRegistro, boolean vip, String nombre,
               char genero, int edad, String direccion) {
    super(nombre, genero, edad, direccion);
    this.idCliente = ++Cliente.contadorCliente;
    this.fechaRegistro = fechaRegistro;
    this.vip = vip;
}

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    
}
    
    
    
