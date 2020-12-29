/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Model;
import Model.Pessoa;
import Model.Animal;
import java.util.ArrayList;

/**
 *
 * @author antonio
 */
public class Cliente extends Pessoa{
    private int ID;
    private ArrayList<Animal> animais;

    public int getID() {
        return ID;
    }
    
    public void insertAnimal(Animal animal){
        animais.add(animal);
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public ArrayList<Animal> getAnimais() {
        return animais;
    }

    public void setAnimais(ArrayList<Animal> animais) {
        this.animais = animais;
    }

    public Cliente(int ID, ArrayList<Animal> animais, String nome, String CPF, Endereço endereço, String celular) {
        super(nome, CPF, endereço, celular);
        this.ID = ID;
        this.animais = animais;
    }

    
    
}
