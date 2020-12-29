/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package quadilatero;
import ponto.Ponto;

/**
 *
 * @author unifansilva
 */
public class Quadrilatero {
    private Ponto p1;
    private Ponto p2;
    private Ponto p3;
    private Ponto p4;

    public Quadrilatero() {
    }

    public Quadrilatero(Ponto p1, Ponto p2, Ponto p3, Ponto p4) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
        this.p4 = p4;
    }

    public Ponto getP1() {
        return p1;
    }

    public void setP1(Ponto p1) {
        this.p1 = p1;
    }

    public Ponto getP2() {
        return p2;
    }

    public void setP2(Ponto p2) {
        this.p2 = p2;
    }

    public Ponto getP3() {
        return p3;
    }

    public void setP3(Ponto p3) {
        this.p3 = p3;
    }

    public Ponto getP4() {
        return p4;
    }

    public void setP4(Ponto p4) {
        this.p4 = p4;
    }
    
    

}
