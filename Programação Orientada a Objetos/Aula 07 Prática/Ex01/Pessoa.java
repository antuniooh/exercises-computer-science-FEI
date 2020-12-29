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
public class Pessoa {

    private String nome;
    private String sobrenome;
    private int idade;
    private int CPF;

    public Pessoa(String nome, String sobrenome, int idade, int CPF) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = idade;

        if(!(CPF > 0))
        {
            throw new CpfException("CPF Apresenta caracteres inválidos");
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getCPF() {
        return CPF;
    }

    public void setCPF(int CPF) {
        this.CPF = CPF;
    }

}
