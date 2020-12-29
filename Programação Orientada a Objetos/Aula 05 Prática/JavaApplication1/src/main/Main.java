/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;
import java.util.Scanner;
import pessoa.Pessoa;
import aluno.Aluno;

/**
 *
 * @author unifansilva
 */
public class Main {
    public static Scanner input;
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        input = new Scanner(System.in);

        System.out.printf("\nDigite a idade: ");
        int idade =  Integer.parseInt(input.nextLine());
        System.out.printf("\nDigite o nome: ");
        String nome = input.nextLine();
        System.out.printf("\nDigite o sobrenome: ");
        String sobrenome = input.nextLine();
        System.out.printf("\nDigite o curso: ");
        String curso = input.nextLine();
        
        Aluno p1 = new Aluno();
        p1.print();
        Aluno p2 = new Aluno(nome,sobrenome,idade,curso);
        p2.print();
        
    }
    
}
