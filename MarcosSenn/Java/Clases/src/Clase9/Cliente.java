package Clase9;

import java.util.Date;

public class Cliente extends Persona {
    private static int clientIdCounter = 0;
    private Date registrationDate;
    private boolean isVip;

    public Cliente(String name, char gender, int age, String address, Date registrationDate, boolean isVip) {
        super(name, gender, age, address);
        clientIdCounter++;
        this.registrationDate = registrationDate;
        this.isVip = isVip;
    }

    public int getClientId() {
        return clientIdCounter;
    }

    public Date getRegistrationDate() {
        return registrationDate;
    }

    public void setRegistrationDate(Date registrationDate) {
        this.registrationDate = registrationDate;
    }

    public boolean isVip() {
        return isVip;
    }

    public void setVip(boolean isVip) {
        this.isVip = isVip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("registrationDate=").append(registrationDate);
        sb.append(", isVip=").append(isVip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}
