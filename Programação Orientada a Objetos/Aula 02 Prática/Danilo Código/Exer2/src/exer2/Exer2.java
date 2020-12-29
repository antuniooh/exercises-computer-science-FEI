
package exer2;

import java.util.Scanner;

public class Exer2 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        Swapper troca = new Swapper();
        
        troca.setX(Float.parseFloat(entrada.nextLine()));
        troca.setY(Float.parseFloat(entrada.nextLine()));
        
        troca.swap();
        
        System.out.println(troca.getX() + " " + troca.getY());   
    }
}
