/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;
import Model.Endereço;

/**
 *
 * @author antonio
 */
public class Pessoa extends Mamifero{
    private String nome;
    private String CPF;
    private Endereço endereço;
    private String celular;

    public Pessoa() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
        this.CPF = CPF;
    }


    public Endereço getEndereço() {
        return endereço;
    }

    public void setEndereço(Endereço endereço) {
        this.endereço = endereço;
    }

    public Pessoa(String nome, String CPF, Endereço endereço, String celular) {
        this.nome = nome;
        this.CPF = CPF;
        this.endereço = endereço;
        this.celular = celular;
    }



    public String getCelular() {
        return celular;
    }

    public void setCelular(String celular) {
        this.celular = celular;
    }
    
    
    
    
    
}
