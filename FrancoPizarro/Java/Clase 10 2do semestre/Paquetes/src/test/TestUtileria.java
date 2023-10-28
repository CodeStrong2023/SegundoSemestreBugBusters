/*
MANERAS DE IMPORTAR UN PAQUETE
 */
package test;
// import ar.com.codesystem.*; con el * importamos todas las clases que esten dentro de ese paquete
import ar.com.codesystem.Utileria;
//import static ar.com.codesystem.Utileria.imprimir; // solo aplica para métodos estaticos
/**
 *
 * @author Franco
 */
public class TestUtileria {
    public static void main(String[] args) {
        Utileria.imprimir("Saludos a todos los alumnos de la tecnicatura");
//          imprimir("Terminamos en unos minutos");
//            ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando"); // no es recomendable esta forma
    }
}
