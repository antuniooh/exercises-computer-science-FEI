package POO;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class Ex2 
{
    private final Scanner input;
    private int num1, num2, num3;
    private final int[] list = new int[3];
    
    public Ex2()
    {
        input = new Scanner(System.in);
    }
    
    public void getNum()
    {
        System.out.printf("Digite o primeiro numero: ");
        num1 = input.nextInt();
        System.out.printf("Digite o segundo numero: ");
        num2 = input.nextInt();
        System.out.printf("Digite o terceiro numero: ");
        num3 = input.nextInt();
    }
    
    public void getOrder()
    {
        list[0] = num1;
        list[1] = num2;
        list[2] = num3;
        
        for(int i = 0; i < 3; i++){
            for(int j = i + 1; j < 3; j++){
                if(list[i] < list[j]){
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
    }
    
    public void printList(){
        System.out.printf("Ordem: ");
        for(int i = 0; i < 3; i++){
            System.out.printf(" %3d", list[i]);
        }
        System.out.printf("\n");
    }
    
}
