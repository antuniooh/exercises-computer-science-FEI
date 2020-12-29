
package Ex06;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static Scanner input;
    
    public static void main(String[] args) {
        input = new Scanner(System.in);
        
        ArrayList<ContaCorrente> banco = new ArrayList<>();

        for(int i = 0; i < 10; i++)
        {
            banco.add(new ContaCorrente(10*i));
        }
        for(ContaCorrente i: banco){
            i.depositar(1000);
            System.out.printf(i.getSaldo() + "\n");
            i.sacar(500);
            System.out.printf(i.getSaldo() + "\n");
            System.out.printf("=====================================\n");

        }
    }
}
