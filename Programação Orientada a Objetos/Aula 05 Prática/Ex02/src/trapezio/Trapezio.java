/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package trapezio;
import quadilatero.Quadrilatero;
import ponto.Ponto;
import java.lang.Math;

/**
 *
 * @author unifansilva
 */
public class Trapezio extends Quadrilatero{

    public Trapezio() {
    }

    public Trapezio(Ponto p1, Ponto p2, Ponto p3, Ponto p4) {
        super(p1, p2, p3, p4);
    }
    
    public double area(Ponto p1, Ponto p2, Ponto p3, Ponto p4)
    {
        double b = distancia(p1, p2);
        double B = distancia(p4, p3);
        double h = distancia(p1, p4);
        return (h*(B + b))/2.0;                
    }
    
    public double distancia(Ponto p1, Ponto p2)
    {
        double dist = Math.sqrt(Math.pow(p1.getX() - p2.getX(),2)  + Math.pow(p1.getY() - p2.getY(),2));
        return dist;
    }
    
}
