/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package politico;

/**
 *
 * @author unifansilva
 */
public class Politico {
    private String nome;
    private String partido;
    private String estado;
    private String funcao;

    public Politico(String nome, String partido, String estado, String funcao) {
        this.nome = nome;
        this.partido = partido;
        this.estado = estado;
        this.funcao = funcao;
    }

    public Politico(String nome, String partido, String estado) {
        this.nome = nome;
        this.partido = partido;
        this.estado = estado;
    }

    
    
    public Politico() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getPartido() {
        return partido;
    }

    public void setPartido(String partido) {
        this.partido = partido;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public String getFuncao() {
        return funcao;
    }

    public void setFuncao(String funcao) {
        this.funcao = funcao;
    }
    
    public void apresentacao()
    {
        System.out.println("==========================");
        System.out.println("Nome: " + this.getNome());
        System.out.println("Partido: " + this.getPartido());
        System.out.println("Função: " + this.getFuncao());
        System.out.println("Estado: " + this.getEstado());
    }
    
}
