package POO;

import java.util.Scanner;

public class Ex6
{
    private final Scanner input;
    public int P, R;
    
    public Ex6()
    {
        input = new Scanner(System.in);
    }
    
    public void CaiCaiBalao()
    {
        System.out.println("P: ");
        P = input.nextInt();
        System.out.println("R: ");
        R = input.nextInt();
        
        if(P == 0)
        {
            System.out.println("A bolinha cairá no caminho C");
        }
        else
        {
            if(R == 0)
            {
                System.out.println("A bolinha cairá no caminho B");
            }
            else
            {
                System.out.println("A bolinha cairá no caminho A");
            }
        }
        
        System.out.printf("\n");
    }
}
