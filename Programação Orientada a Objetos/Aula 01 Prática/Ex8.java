package POO;

import java.util.Scanner;

public class Ex8 
{
    private final Scanner input;
    
    public Ex8()
    {
        input = new Scanner(System.in);
    }
    
    public void BohemianRhapsody(){
        int num;
        
        for(int i = 0; i < 5; i++){
            System.out.printf("Digite o %dº numero: ", i+1);
            num = input.nextInt();
            
            System.out.printf("Conversão: ");
            for(int j = 0; j < num; j++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }
        
        System.out.printf("\n");
    }
}
