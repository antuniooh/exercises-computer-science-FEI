package javaapplication5;

import java.util.Scanner;

public class Main {

    public static Data setData(int dia, int mes, int ano)
    {
        Data data = new Data();

        data.setDia(dia);
        data.setMes(mes);
        data.setAno(ano);

        return data;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Data data = new Data();
       
        System.out.println("=================================");
        System.out.printf("Digite o dia Atual\n");
        int dia =  Integer.parseInt(input.nextLine());

        System.out.printf("Digite o mês Atual\n");
        int mes =  Integer.parseInt(input.nextLine());

        System.out.printf("Digite o ano Atual\n");
        int ano =  Integer.parseInt(input.nextLine());

        data = setData(dia, mes, ano);

        data.exibeData();

    }
    
}
