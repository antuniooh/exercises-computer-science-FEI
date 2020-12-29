
package Ex02;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Formas forma; 
        Scanner entrada = new Scanner ( System.in );
        String formaEscolhida = entrada.nextLine(); 

        if(formaEscolhida.equals("Retangulo"))
            forma = new Retangulo(5,4);
        else
            forma = new Circulo(5);

        forma.print();
        entrada.close();
    }
}
