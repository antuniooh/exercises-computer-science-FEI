/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package navioMercante;
import navio.Navio;
/**
 *
 * @author unifansilva
 */
public class NavioMercante extends Navio{
    private double capacidadeCarga;
    private double carga;

    public NavioMercante(double capacidadeCarga, double carga, int numTripulantes, String nome) {
        super(numTripulantes, nome);
        this.capacidadeCarga = capacidadeCarga;
        this.carga = carga;
    }
    
    

    public double getCapacidadeCarga() {
        return capacidadeCarga;
    }

    public void setCapacidadeCarga(double capacidadeCarga) {
        this.capacidadeCarga = capacidadeCarga;
    }

    public double getCarga() {
        return carga;
    }

    public void setCarga(double carga) {
        this.carga = carga;
    }
    
    public void carregamento(int valor)
    {
        if(this.carga + valor <= this.capacidadeCarga)
        {
            this.carga+=valor;
        }
        else
        {
            System.out.println("Impossivel adicionar a carga");
        }
    }
    
    
}
