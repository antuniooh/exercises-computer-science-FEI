/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package portaAvioes;
import navioDeGuerra.NavioDeGuerra;
/**
 *
 * @author unifansilva
 */
public class PortaAvioes extends NavioDeGuerra{
    protected int numAvioes;

    public PortaAvioes(int numAvioes, double blindagem, double ataque, int numTripulantes, String nome) {
        super(blindagem, ataque, numTripulantes, nome);
        this.numAvioes = numAvioes;
    }
    
    public int getNumAvioes() {
        return numAvioes;
    }

    public void setNumAvioes(int numAvioes) {
        this.numAvioes = numAvioes;
    }
    
    
    
    public void poderDeFogo()
    {
        System.out.println("==========================");        
        System.out.println("Poder de Fogo: " + this.ataque);
        System.out.println("Avioes: " + this.numAvioes);
    }
}
