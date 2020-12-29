/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;
import ponto.Ponto;
import retangulo.Retangulo;
import paralelogramo.Paralelogramo;
import trapezio.Trapezio;
import quadrado.Quadrado;
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
        Retangulo r1 = new Retangulo(new Ponto(5,0),new Ponto(5,5),new Ponto(0,5),new Ponto(0,0));
        System.out.println("AREA: " +r1.area(r1.getP1(), r1.getP2(), r1.getP3(), r1.getP4()));
        
        Quadrado q1 = new Quadrado(new Ponto(5,0),new Ponto(5,5),new Ponto(0,5),new Ponto(0,0));
        System.out.println("AREA: " +q1.area(q1.getP1(), q1.getP2(), q1.getP3(), q1.getP4()));
        
        Paralelogramo p1 = new Paralelogramo(new Ponto(5,0),new Ponto(5,5),new Ponto(0,5),new Ponto(0,0));
        System.out.println("AREA: " +p1.area(p1.getP1(), p1.getP2(), p1.getP3(), p1.getP4()));
        
        Trapezio t1 = new Trapezio(new Ponto(5,0),new Ponto(5,5),new Ponto(0,5),new Ponto(0,0));
        System.out.println("AREA: " +t1.area(t1.getP1(), t1.getP2(), t1.getP3(), t1.getP4()));
        
    }
    
}
