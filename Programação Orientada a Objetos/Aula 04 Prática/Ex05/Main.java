
package Ex05;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static Scanner input;
    
    public static void main(String[] args) {
        input = new Scanner(System.in);
        
        ArrayList<Peça> xadrez = new ArrayList<>();

        //add peões
        for(int i = 0; i < 2; i++){
            int numero1 = 0;
            int numero2 = 0;
            String cor = "";

            //branco
            if(i == 0)
            {
                numero1 = 2;
                numero2 = 1;
                cor = "Branco";
            }
            else
            {
                numero1 = 7;
                numero2 = 8;
                cor = "Preto";
            }
                xadrez.add(new Peça("Peões", cor, "a" + numero1));
                xadrez.add(new Peça("Peões", cor, "b" + numero1));
                xadrez.add(new Peça("Peões", cor, "c" + numero1));
                xadrez.add(new Peça("Peões", cor, "d" + numero1));
                xadrez.add(new Peça("Peões", cor, "e" + numero1));
                xadrez.add(new Peça("Peões", cor, "f" + numero1));
                xadrez.add(new Peça("Peões", cor, "g" + numero1));
                xadrez.add(new Peça("Peões", cor, "h" + numero1));

                xadrez.add(new Peça("Torre", cor, "a" + numero2));
                xadrez.add(new Peça("Torre", cor, "h" + numero2));

                xadrez.add(new Peça("Cavalo", cor, "b" + numero2));
                xadrez.add(new Peça("Cavalo", cor, "g" + numero2));

                xadrez.add(new Peça("Bispo", cor, "c" + numero2));
                xadrez.add(new Peça("Bispo", cor, "f" + numero2));

                xadrez.add(new Peça("Rainha", cor, "d" + numero2));
                xadrez.add(new Peça("Rei", cor, "e" + numero2));
            
        }
        System.out.printf("\nDigite a posicao: ");
        String posicaoDelete = input.nextLine();
        for(int i = 0; i < xadrez.size(); i++)
            {
                if(xadrez.get(i).getPosicao().equals(posicaoDelete))
                {                
                    xadrez.remove(i);
                        break;
                    }
                }
        System.out.printf("\nDeletado com sucesso...\n");
 
        System.out.printf("\nImprimindo todos...\n");
            for (Peça element : xadrez) 
                System.out.println(element.toString() + "\n");
            }
            
}
