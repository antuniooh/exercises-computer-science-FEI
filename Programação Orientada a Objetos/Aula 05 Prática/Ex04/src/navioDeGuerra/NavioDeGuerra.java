/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package navioDeGuerra;
import navio.Navio;
/**
 *
 * @author unifansilva
 */
public class NavioDeGuerra extends Navio{
    protected double blindagem;
    protected double ataque;

    public NavioDeGuerra() {
    }

    public NavioDeGuerra(double blindagem, double ataque, int numTripulantes, String nome) {
        super(numTripulantes, nome);
        this.blindagem = blindagem;
        this.ataque = ataque;
    }

    public double getBlindagem() {
        return blindagem;
    }

    public void setBlindagem(double blindagem) {
        this.blindagem = blindagem;
    }

    public double getAtaque() {
        return ataque;
    }

    public void setAtaque(double ataque) {
        this.ataque = ataque;
    }
    
    public void exibirArmas()
    {
        System.out.println("Blindagem: " + this.blindagem + " Ataque: " + this.ataque);
    }
    
    public void poderDeFogo()
    {
        System.out.println("==========================");        
        System.out.println("Poder de Fogo: " + this.ataque);
    }
    
}
