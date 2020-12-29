/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex02;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

/**
 *
 * @author unifansilva
 */
public class Main {

    public static Scanner input;

    public static void Gui() {
        System.out.printf(""
                + "\n=========================================================="
                + "\n n [Nova Entrada]"
                + "\n d [Apaga Registro da Agenda]"
                + "\n p [Imprime toda a agenda]"
                + "\n q [Sai do programa]"
                + "\n==========================================================");
    }

    public static void main(String[] args) throws IOException {
        input = new Scanner(System.in);

        ArrayList<PhoneBook> pb = new ArrayList<>();
        boolean run = true;

        while (run) {
            Gui();

            System.out.printf("\nDigite a opção: ");
            String choice = input.nextLine();

            switch (choice) {
                case "q":
                    System.out.printf("\nSaindo...\n");
                    run = false;
                    break;
                case "n":
                    System.out.printf("\nDigite o nome: ");
                    String nome = input.nextLine();
                    System.out.printf("\nDigite o telefone: ");
                    String telefone = input.nextLine();

                    try {
                        String allText = "";

                        try {
                            FileReader arquivoLeitura = new FileReader("PhoneBook.txt");
                            BufferedReader br = new BufferedReader(arquivoLeitura);
                            String line;

                            while ((line = br.readLine()) != null) {
                                allText += line +"\n";
                            }
                        } catch (Exception e) {}

                        FileWriter arquivo = new FileWriter("PhoneBook.txt");

                        PrintWriter escritaArquivo = new PrintWriter(arquivo);

                        escritaArquivo.println(allText);
                        escritaArquivo.println(nome + " " + telefone);

                        arquivo.close();
                    } catch (Exception e) {
                    }

                    System.out.printf("\n Usuário criado com sucesso\n");
                    break;
                case "d":
                    System.out.printf("\nDigite o nome: ");
                    String nomeDelete = input.nextLine();

                    try {
                        String allText = "";

                        try {
                            FileReader arquivoLeitura = new FileReader("PhoneBook.txt");
                            BufferedReader br = new BufferedReader(arquivoLeitura);

                            String line;
                            while ((line = br.readLine()) != null) {
                                if (!line.contains(nomeDelete)) {
                                    allText += line +"\n";
                                }
                            }
                        } catch (Exception e) {
                        }

                        FileWriter arquivo = new FileWriter("PhoneBook.txt");
                        PrintWriter escritaArquivo = new PrintWriter(arquivo);

                        escritaArquivo.println(allText);
                        arquivo.close();

                    } catch (Exception e) {
                    }

                    System.out.printf("\nDeletado com sucesso...\n");
                    break;
                case "p":
                    System.out.printf("\nImprimindo todos...\n");
                    try {
                        FileReader arquivoLeitura = new FileReader("PhoneBook.txt");
                        BufferedReader br = new BufferedReader(arquivoLeitura);
                        String line;

                        while ((line = br.readLine()) != null) {
                            System.out.println(line);
                        }
                    } catch (Exception e) {
                    }
                    break;
                default:
                    break;
            }
        }
    }

}
