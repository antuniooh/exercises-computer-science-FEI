package Exercicio02;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        System.out.println("=================================");
        System.out.println("Qual a opção desejada?");
        System.out.println("1 - MM/DD/YYYY");
        System.out.println("2 - Mês Dia, Ano");
        System.out.println("3 - DiaTotal Ano");
        System.out.println(">");
        int opc =  Integer.parseInt(input.nextLine());

        switch(opc){
            case 1:
                System.out.printf("Digite o mês Atual\n");
                int mes1 =  Integer.parseInt(input.nextLine());

                System.out.printf("Digite o dia Atual\n");
                int dia1 =  Integer.parseInt(input.nextLine());

                System.out.printf("Digite o ano Atual\n");
                int ano1 =  Integer.parseInt(input.nextLine());

                Data data = new Data(mes1, dia1, ano1);
                data.printAll();
                break;
            case 2:
                System.out.printf("Digite o mês Atual\n");
                String mes2 =  input.nextLine();

                System.out.printf("Digite o dia Atual\n");
                int dia2 =  Integer.parseInt(input.nextLine());

                System.out.printf("Digite o ano Atual\n");
                int ano2 =  Integer.parseInt(input.nextLine());

                Data data2 = new Data(mes2, dia2, ano2);
                data2.printAll();
                break;
            case 3:
                System.out.printf("Digite o dia Total\n");
                int dia3 =  Integer.parseInt(input.nextLine());

                System.out.printf("Digite o ano Atual\n");
                int ano3 =  Integer.parseInt(input.nextLine());

                Data data3 = new Data(dia3, ano3);
                data3.printAll();
                break;
        }
    }
    
}
