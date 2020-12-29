/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;
import java.util.ArrayList;
import java.util.Random;

/**
 *
 * @author antonio
 */
public class Pangrama {
    ArrayList<String> p = new ArrayList();
    Random rand = new Random();
    private int erro = 0;
    private int acerto = 0;
    private int index = 0;

    public int getErro() {
        return erro;
    }

    public void setErro(int erro) {
        this.erro = erro;
    }

    public int getAcerto() {
        return acerto;
    }

    public void setAcerto(int acerto) {
        this.acerto = acerto;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    
    
    
    public void createPangramas(){
        p.add("The quick brown fox jumps over the lazy dog");
        p.add("Um pequeno jabuti xereta viu dez cegonhas felizes");
        p.add("Blitz prende ex vesgo com cheque fajuto");
        p.add("Gazeta publica hoje no jornal uma breve nota de faxina na quermesse");
        p.add("Zebras caolhas de Java querem passar fax para moças gigantes de New York");
    }
    
    public String takePangran(){
        int index = rand.nextInt(p.size());
        String pangrama = p.get(index);
        return pangrama;
    }
    
    public void checkValue(String string, char character){
        System.out.println(index);
        if(Character.toLowerCase(string.charAt(index)) ==  character){
            acerto++;
            index++;
        }
        else
            erro++;
    }
    
    
}
