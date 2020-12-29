/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex07;

/**
 *
 * @author unifansilva
 */
public class Bancos {
    private String tecido;
    private String cor;

    public Bancos(String tecido, String cor) {
        this.tecido = tecido;
        this.cor = cor;
    }

    public Bancos() {
    }

    public String getTecido() {
        return tecido;
    }

    public void setTecido(String tecido) {
        this.tecido = tecido;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }
    
    
}
