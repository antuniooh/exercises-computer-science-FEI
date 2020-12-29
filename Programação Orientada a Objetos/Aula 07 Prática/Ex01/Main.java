package Ex01;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author antonio
 */
import java.util.Scanner;

public class Main {

    private static Object e;

    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        boolean run = true;
        
        Pessoa p;
        
        System.out.println("Entrada de dados\n=======================================");
        System.out.println("Digite o nome: ");
        String nome = input.nextLine();
        System.out.println("Digite o sobrenome: ");
        String sobrenome = input.nextLine();
        System.out.println("Digite a idade: ");
        int idade = Integer.parseInt(input.nextLine());

        while(run) {
            try {
                System.out.println("Digite o CPF: ");
                int cpf = Integer.parseInt(input.nextLine());
                run = false;

                p = new Pessoa(nome, sobrenome, idade, cpf);

            } catch (RuntimeException ex) {
                run = true;
            }
        }
    
    }
}
