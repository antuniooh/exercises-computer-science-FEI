/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;

/**
 *
 * @author antonio
 */
public class Veterinario extends Pessoa{
    private String CRV;
    private String especialidade;

    public Veterinario(String CRV, String especialidade, String nome, String CPF, Endereço endereço, String celular) {
        super(nome, CPF, endereço, celular);
        this.CRV = CRV;
        this.especialidade = especialidade;
    }

    

    public String getCRV() {
        return CRV;
    }

    public void setCRV(String CRV) {
        this.CRV = CRV;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }
    
    
}
