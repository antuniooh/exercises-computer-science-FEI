package javaapplication1;

import java.util.Scanner;

public class Main {

    public static Pessoa setPeople(String cpf, String name, int idade)
    {
        Pessoa p = new Pessoa();

        p.setCpf(cpf);
        p.setName(name);
        p.setIdade(idade);

        return p;
    }

    public static void retorno(Pessoa p)
    {
        System.out.println("=================================");
        System.out.printf("Nome: %s\n", p.getName());
        System.out.printf("CPF: %s\n", p.getCpf());
        System.out.printf("Idade: %d\n", p.getIdade());
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Pessoa p1 = new Pessoa();
        Pessoa p2 = new Pessoa(); 
        Pessoa p3 = new Pessoa();
        
        for(int i = 1; i < 4; i++){
            System.out.println("=================================");

            System.out.printf("Digite o nome da pessoa %d: ", i);
            String name = input.nextLine();

            System.out.printf("Digite o cpf da pessoa %d :", i);
            String cpf = input.nextLine();

            System.out.printf("Digite a Idade da pessoa %d: ", i);
            int idade =  Integer.parseInt(input.nextLine());

            switch (i) {
                case 1:
                    p1 = setPeople(cpf, name, idade);
                    break;
                case 2:
                    p2 = setPeople(cpf, name, idade);
                case 3:
                    p3 = setPeople(cpf, name, idade);
            }
        }
        retorno(p1);
        retorno(p2);
        retorno(p3);

    }
    
}
