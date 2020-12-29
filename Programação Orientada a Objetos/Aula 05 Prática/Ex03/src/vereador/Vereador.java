/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vereador;
import politico.Politico;

/**
 *
 * @author unifansilva
 */
public class Vereador extends Politico{
     private String municipio;
          
 public Vereador( String nome, String partido, String municipio,String estado) {
        super(nome, partido, estado);
        this.setFuncao("Vereador");
        this.municipio = municipio;
    }

    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }
    
     @Override
        public void apresentacao()
    {
        System.out.println("==========================");
        System.out.println("Nome: " + this.getNome());
        System.out.println("Partido: " + this.getPartido());
        System.out.println("Função: " + this.getFuncao());
        System.out.println("Estado: " + this.getEstado());        
        System.out.println("Municipio: " + this.getMunicipio());
    }
}
    
    

    

    
    
