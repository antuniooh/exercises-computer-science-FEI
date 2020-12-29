package Exercicio3;

import java.util.Scanner;

public class Main {

    public static HeartRates setHeartRates(String name, String sobrenome, int dia, int mes, int ano)
    {
        HeartRates heart = new HeartRates();
        heart.setName(name);
        heart.setSobrenome(sobrenome);
        heart.setDia(dia);
        heart.setMes(mes);
        heart.setAno(ano);
        heart.setIdade();
        heart.setFrequenciaCardiacaMaxima();
        heart.setFrequenciaCardiacaAlvoMin();
        heart.setFrequenciaCardiacaAlvoMax();
       
        return heart;
    }
    
    public static void retorno(HeartRates h)
    {
        System.out.println("=================================");
        System.out.printf("Nome: %s %s\n", h.getName(), h.getSobrenome());
        System.out.printf("Idade: %d anos\n", h.getIdade());
        System.out.printf("Frequencia Cardiaca Maxima: %d \n", h.getFrequenciaCardiacaMaxima());
        System.out.printf("Frequencia Cardiaca Alvo: [%f , %f]\n", h.getFrequenciaCardiacaAlvoMin(), h.getFrequenciaCardiacaAlvoMax());


    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        
        System.out.println("=================================");

        System.out.printf("Digite o nome: ");
        String name = input.nextLine();

        System.out.printf("Digite o sobrenome: ");
        String sobrenome = input.nextLine();

        System.out.printf("Digite o dia de nascimento: ");
        int dia =  Integer.parseInt(input.nextLine());
        System.out.printf("Digite o mes de nascimento: ");
        int mes =  Integer.parseInt(input.nextLine());
        System.out.printf("Digite o ano de nascimento: ");
        int ano =  Integer.parseInt(input.nextLine());

        HeartRates h = new HeartRates(name, sobrenome, dia, mes, ano);
        h.setIdade();
        h.setFrequenciaCardiacaMaxima();
        h.setFrequenciaCardiacaAlvoMin();
        h.setFrequenciaCardiacaAlvoMax();
        
        retorno(h);

    }
    
}

