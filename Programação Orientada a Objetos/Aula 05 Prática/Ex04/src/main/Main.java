/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;
import navioMercante.NavioMercante;
import portaAvioes.PortaAvioes;
import cruzador.Cruzador;
/**
 *
 * @author unifansilva
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        NavioMercante navioMercante = new NavioMercante(100,0,5,"Navio Cargueiro");
        navioMercante.exibirInfoGeral();
        navioMercante.carregamento(50);
        System.out.println("Carga Atual: " + navioMercante.getCarga());
        
        PortaAvioes portaAvioes = new PortaAvioes(10,100,100,5,"Navioptero");
        portaAvioes.exibirInfoGeral();
        portaAvioes.exibirArmas();
        portaAvioes.poderDeFogo();
        
        Cruzador cruzador = new Cruzador(10,100,100,5,"Cruzavio");
        cruzador.exibirInfoGeral();
        cruzador.exibirArmas();
        cruzador.poderDeFogo();
                
       


    }
    
}
