/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex03;

import java.util.Scanner;
import java.util.Random;

/**
 *
 * @author antonio
 */
public class Main {

    public static Scanner input;

    public static void main(String[] args) {
        input = new Scanner(System.in);
        System.out.printf("\nDigite o nome: ");
        String nome = input.nextLine();
        Factory factory = Singleton.getInstance();

        Random value = new Random();        
        Output output = factory.getOutput(value.nextInt(2));
        output.print(nome);
    }
}
