package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0;
        while(conteo < 3) {
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        
        //Uso de las palabras break y continue en las estiquetas (labels)
        int contando;
        inicio:
        for(contando = 0 ; contando < 7 ; contando++) {
            if(contando % 2 == 0) {
                System.out.println("Contando" + contando);
                break inicio;
            } 
        }
        

        
        for(contando = 0 ; contando < 7 ; contando++) {
            if(contando % 2 != 0) {
               continue;
            } 
             System.out.println("Contando" + contando);
        }
    }
}
