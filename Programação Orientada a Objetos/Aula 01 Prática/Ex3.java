package POO;

import java.util.Scanner;

public class Ex3 {
    private final Scanner input;
    
    public Ex3(){
        input = new Scanner(System.in);
       
    }
    
    public void showOdd(){
        System.out.println("Numeros Impares:\n");
        for(int i = 0; i <= 1000; i++){
            if(i % 2 != 0){
                System.out.printf("%5d\n", i);
            }
        }
        System.out.printf("\n");
    }
}
