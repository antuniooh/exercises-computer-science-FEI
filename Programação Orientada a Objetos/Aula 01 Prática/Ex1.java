package POO;

import java.util.Scanner;

public class Ex1 {
    private final Scanner input;
    
    public Ex1(){
        input = new Scanner(System.in);
    }
    
    public void Solution(){
        System.out.printf("Digite o primeiro numero: ");
        int num1 = input.nextInt();
        
        System.out.printf("Digite o segundo numero: ");
        int num2 = input.nextInt();
        
        System.out.printf("Digite o terceiro numero: ");
        int num3 = input.nextInt();
        
        int prod = num1 * num2 * num3;
        
        System.out.printf("Produto = %d\n", prod);
    }
}
