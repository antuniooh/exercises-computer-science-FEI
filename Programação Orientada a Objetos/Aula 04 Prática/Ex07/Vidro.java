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
public class Vidro {
    private String material;
    private boolean sufilm;

    public Vidro() {
    }

    public Vidro(String material, boolean sufilm) {
        this.material = material;
        this.sufilm = sufilm;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public boolean isSufilm() {
        return sufilm;
    }

    public void setSufilm(boolean sufilm) {
        this.sufilm = sufilm;
    }
    
    
    
}
