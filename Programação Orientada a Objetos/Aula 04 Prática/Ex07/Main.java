
package Ex07;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static Scanner input;
    
    public static void main(String[] args) {
       input = new Scanner(System.in);
   
       AirBags airbag = new AirBags("Marca Airbag","Algodão");
       Bancos bancos = new Bancos("Couro","Branco");
       Documentação documentacao = new Documentação("SP",2019);
       Extintor extintor = new Extintor("Extintor", 50);
       Lataria lataria = new Lataria("Vermelho", "Plástico");
       Modelo modelo = new Modelo("FIAT", "Argo");
       Motor motor = new Motor("FIAT", 1500);
       ArrayList<Rodas> rodas = new ArrayList<>();
        for(int i = 0; i < 4; i++)
            rodas.add(new Rodas("Bridgstone", 18,"Liga Leve"));
       TetoSolar tetoSolar = new TetoSolar("Teto",150);
       Vidro vidro = new Vidro("Temperado", true);
       
       Carro carro = new Carro(airbag, bancos, documentacao,extintor,lataria,modelo,motor,rodas,tetoSolar,vidro);
       
       System.out.println(carro.toString());


    }
}
