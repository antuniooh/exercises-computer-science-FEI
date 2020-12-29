package Exercicio5;

import java.util.Scanner;

public class Main {

    public static void retorno(Complex r)
    {
        System.out.println("=================================");
        System.out.printf("%s\n", r.retornoString());
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Complex r1 = new Complex(1,2);
        Complex r2 = new Complex(3,4);
        Complex resul = new Complex();
        
        resul = resul.somar(r1, r2);
        retorno(resul);
        resul = resul.subtrair(r1, r2);
        retorno(resul);

    }
    
}

