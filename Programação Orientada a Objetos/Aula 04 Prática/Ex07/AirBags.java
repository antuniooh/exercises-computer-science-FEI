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
public class AirBags {
    private String marca;
    private String tecido;

    public AirBags() {
    }

    public AirBags(String marca, String tecido) {
        this.marca = marca;
        this.tecido = tecido;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTecido() {
        return tecido;
    }

    public void setTecido(String tecido) {
        this.tecido = tecido;
    }
    
    
}
