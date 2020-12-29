package POO;

import java.util.Scanner;

public class Ex4 {
    private final Scanner input;
    
    public Ex4(){
        input = new Scanner(System.in);    
    }
    
    public void getNumbers(){
        int qtd = 0;
        
        for(int i = 0; i < 20; i++){
            System.out.printf("Digite o numero %d: ", i);
            float num = input.nextFloat();
            
            if(num > 0.0f){
                System.out.printf("POSITIVO: %.2f\n", num);
                qtd++;
            }
        }
        
        System.out.printf("Quantia de numeros positivos: %d\n", qtd);
        System.out.printf("\n");
    }
    
    
}
