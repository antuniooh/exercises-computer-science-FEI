package javaapplication3;

import java.util.Scanner;

public class Main {

    public static Rectangle setRectangle(int lado1, int lado2)
    {
        Rectangle r = new Rectangle();

        r.setLado1(lado1);
        r.setLado2(lado2);

        return r;
    }

    public static void retorno(Rectangle r)
    {
        System.out.println("=================================");
        System.out.printf("X: %d e Y: %d\n", r.getLado1(), r.getlado2());
        System.out.printf("Area: %d\n", r.area());
        System.out.printf("Perimetro: %d\n", r.perimetro());
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Rectangle ret1 = new Rectangle();
        Rectangle ret2 = new Rectangle();

        for(int i = 1; i < 3; i++){
            System.out.println("=================================");

            System.out.printf("Digite o lado1 do retangulo %d: ", i);
            int lado1 =  Integer.parseInt(input.nextLine());

            System.out.printf("Digite o lado2 do retangulo %d: ", i);
            int lado2 =  Integer.parseInt(input.nextLine());

            switch (i) {
                case 1:
                    ret1 = setRectangle(lado1, lado2);
                    break;
                case 2:
                    ret2 = setRectangle(lado1, lado2);
                    break;
            }
        }
        retorno(ret1);
        retorno(ret2);

    }
    
}
