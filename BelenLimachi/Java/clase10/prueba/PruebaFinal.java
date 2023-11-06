package clase10.prueba;

import clase10.Persona;

public class PruebaFinal {
    public static void main(String[] args) {
        final int miDni = 37216301;
        System.out.println("miDni = " + miDni);

    
        //Persona.CONSTANTE_AQUI = 5; // No se modifica.
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);


        final Persona persona1 = new Persona();
        //persona1 = new Persona(); 
        persona1.setNombre("Belen");
        System.out.println("persona1 = " + persona1.getNombre());

        persona1.setNombre("Brisa"); // Sí se puede modificar.
        System.out.println("persona1 = " + persona1.getNombre());
    }

}
