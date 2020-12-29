package javaapplication2;

import java.util.Scanner;

public class Main {

    public static Swapper setSwapper(final float x, final float y)
    {
        final Swapper s = new Swapper();

        s.setX(x);
        s.setY(y);

        return s;
    }

    public static void retorno(final Swapper s)
    {
        System.out.println("=================================");
        System.out.printf("X: %f\n", s.getX());
        System.out.printf("Y: %f\n", s.getY());
    }
    
    public static void main(final String[] args) {
        final Scanner input = new Scanner( System.in );

        Swapper troca = new Swapper();
        
            System.out.println("=================================");

            System.out.printf("Digite o x: ");
            final float x =  Float.parseFloat(input.nextLine());
            System.out.printf("Digite o y: ");
            final float y =  Float.parseFloat(input.nextLine());

            troca = setSwapper(x, y);
        
        retorno(troca);
        troca.swap();
        retorno(troca);
    }
    
}
