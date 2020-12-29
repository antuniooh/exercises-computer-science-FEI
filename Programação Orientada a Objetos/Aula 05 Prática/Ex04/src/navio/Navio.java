/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package navio;

/**
 *
 * @author unifansilva
 */
public class Navio {
    protected int numTripulantes;
    protected String nome;

    public Navio() {
    }

    public Navio(int numTripulantes, String nome) {
        this.numTripulantes = numTripulantes;
        this.nome = nome;
    }

    public int getNumTripulantes() {
        return numTripulantes;
    }

    public void setNumTripulantes(int numTripulantes) {
        this.numTripulantes = numTripulantes;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public void exibirInfoGeral()
    {
        System.out.println("==========================");        
        System.out.println("Nome: " + this.getNome());
        System.out.println("Tripulantes: " + this.getNumTripulantes());
    }
}
