/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex07;
import java.util.ArrayList;

/**
 *
 * @author unifansilva
 */
public class Carro {
    private AirBags airbag;
    private Bancos bancos;
    private Documentação documentacao;
    private Extintor extintor;
    private Lataria lataria;
    private Modelo modelo;
    private Motor motor;
    private ArrayList<Rodas> rodas;
    private TetoSolar tetoSolar;
    private Vidro vidro; 

    public Carro(AirBags airbag, Bancos bancos, Documentação documentacao, Extintor extintor, Lataria lataria, Modelo modelo, Motor motor, ArrayList<Rodas> rodas, TetoSolar tetoSolar, Vidro vidro) {
        this.airbag = airbag;
        this.bancos = bancos;
        this.documentacao = documentacao;
        this.extintor = extintor;
        this.lataria = lataria;
        this.modelo = modelo;
        this.motor = motor;
        this.rodas = rodas;
        this.tetoSolar = tetoSolar;
        this.vidro = vidro;
    }

    public Carro() {
    }

    public AirBags getAirbag() {
        return airbag;
    }

    public void setAirbag(AirBags airbag) {
        this.airbag = airbag;
    }

    @Override
    public String toString() {
        return "Carro{" + "airbag=" + airbag + ", bancos=" + bancos + ", documentacao=" + documentacao + ", extintor=" + extintor + ", lataria=" + lataria + ", modelo=" + modelo + ", motor=" + motor + ", rodas=" + rodas + ", tetoSolar=" + tetoSolar + ", vidro=" + vidro + '}';
    }

  
    public Bancos getBancos() {
        return bancos;
    }

    public void setBancos(Bancos bancos) {
        this.bancos = bancos;
    }

    public Documentação getDocumentacao() {
        return documentacao;
    }

    public void setDocumentacao(Documentação documentacao) {
        this.documentacao = documentacao;
    }

    public Extintor getExtintor() {
        return extintor;
    }

    public void setExtintor(Extintor extintor) {
        this.extintor = extintor;
    }

    public Lataria getLataria() {
        return lataria;
    }

    public void setLataria(Lataria lataria) {
        this.lataria = lataria;
    }

    public Modelo getModelo() {
        return modelo;
    }

    public void setModelo(Modelo modelo) {
        this.modelo = modelo;
    }

    public Motor getMotor() {
        return motor;
    }

    public void setMotor(Motor motor) {
        this.motor = motor;
    }

    public ArrayList<Rodas> getRodas() {
        return rodas;
    }

    public void setRodas(ArrayList<Rodas> rodas) {
        this.rodas = rodas;
    }

    public TetoSolar getTetoSolar() {
        return tetoSolar;
    }

    public void setTetoSolar(TetoSolar tetoSolar) {
        this.tetoSolar = tetoSolar;
    }

    public Vidro getVidro() {
        return vidro;
    }

    public void setVidro(Vidro vidro) {
        this.vidro = vidro;
    }
    
    
    
}
