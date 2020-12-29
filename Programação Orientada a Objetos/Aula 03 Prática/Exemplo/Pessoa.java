/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

/**
 *
 * @author unifansilva
 */
public class Pessoa {
    private String nome;
    private String endereco;
    private double renda;
    public ContaComum conta;

    public Pessoa() {
    }
    
    public void setConta(ContaComum conta)
    {
        this.conta = conta;
    }
    public void alteraNumConta()
    {
        conta.numero = 5555;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public double getRenda() {
        return renda;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public void setRenda(double renda) {
        this.renda = renda;
    }
    
    
}
