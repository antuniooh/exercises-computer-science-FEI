/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author antonio
 */
public class File {
    private String nome, sobrenome, cpf, idade, sexo;

    public File(String nome, String sobrenome, String cpf, String idade, String sexo) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.idade = idade;
        this.sexo = sexo;
    }

    public File() {
    }
    
    public void addDataToFile(){
        try {
            FileWriter file = new FileWriter("usuarios.txt", true);
            PrintWriter pr = new PrintWriter(file);
            pr.println("Nome: " + nome + " sobrenome: " + sobrenome + " idade: " + idade + " cpf: " + cpf + " sexo: " + sexo);
            file.close();
        } catch (IOException ex) {
            Logger.getLogger(File.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public ArrayList findUser(String cpf){
        ArrayList<String> array = new ArrayList<>();
        boolean find = false;
        try {
            FileReader file = new FileReader("usuarios.txt");
            BufferedReader br = new BufferedReader(file);
            String str;
            String[] words = null;
            while ((str = br.readLine()) != null){
                words = str.split(" ");
                for (String word : words){
                    if(word.equals(cpf)){
                        array.add(str);
                        System.out.println(str);
                        find = true;
                    }
                }
            }
            file.close();
            return array;
        } catch (IOException ex) {
            System.out.println("Ocorreu um erro na leitura do arquivo");
        }
        if (find == false || array.isEmpty()){
            System.out.println("entrou");
            array.add("Nenhum usuario encontrado com este cpf");
        }
        return array;
    }
}
