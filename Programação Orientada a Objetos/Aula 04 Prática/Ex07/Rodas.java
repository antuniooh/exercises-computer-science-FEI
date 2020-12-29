/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex07;

/**
 *
 * @author unifansilva
 */
public class Rodas {
    private String marca;
    private int aro;
    private String ferro;

    public Rodas(String marca, int aro, String ferro) {
        this.marca = marca;
        this.aro = aro;
        this.ferro = ferro;
    }

    public Rodas() {
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAro() {
        return aro;
    }

    public void setAro(int aro) {
        this.aro = aro;
    }

    public String getFerro() {
        return ferro;
    }

    public void setFerro(String ferro) {
        this.ferro = ferro;
    }
    
    
}
