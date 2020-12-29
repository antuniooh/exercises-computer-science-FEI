/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cruzador;
import navioDeGuerra.NavioDeGuerra;
/**
 *
 * @author unifansilva
 */
public class Cruzador extends NavioDeGuerra{
    protected int numCanhoes;

    public int getNumCanhoes() {
        return numCanhoes;
    }

    public void setNumCanhoes(int numCanhoes) {
        this.numCanhoes = numCanhoes;
    }

    public Cruzador(int numCanhoes, double blindagem, double ataque, int numTripulantes, String nome) {
        super(blindagem, ataque, numTripulantes, nome);
        this.numCanhoes = numCanhoes;
    }
    
    @Override
    public void poderDeFogo()
    {
        System.out.println("==========================");
        System.out.println("Poder de Fogo: " + this.ataque);
        System.out.println("Canhôes: " + this.numCanhoes);
    }
    
    
}
