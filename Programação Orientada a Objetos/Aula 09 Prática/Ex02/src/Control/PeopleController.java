/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Control;
import Model.Cliente;
import Model.Veterinario;
import java.util.ArrayList;
import Model.Animal;
import Model.Cachorro;
import Model.Gato;

/**
 *
 * @author antonio
 */
public class PeopleController {
    private ArrayList<Cliente> clientes;
    private ArrayList<Veterinario> veterinarios;

    public PeopleController() {
    }
    
    public void createClients(Cliente c){
        clientes.add(c);
    }
    public void createVeterinary(Veterinario v){
        veterinarios.add(v);
    }
    
    public int retornoIndexClient(int ID){
        int index = 0;
         for(int i = 0; i < clientes.size(); i++)
            {
                if(clientes.get(i).getID() == ID)
                {                
                    index = i;
                    break;
                }
            }
        return index;
    }
    
    public void createPet(int idDono,int ID, int idade, String nome, String tipo, String raca){
        if(tipo == "Cachorro"){
            Cachorro dog = new Cachorro(ID, idade, nome, tipo, raca);
            clientes.get(retornoIndexClient(idDono)).insertAnimal(dog);
        }
        else if(tipo == "Gato"){
            Gato cat = new Gato(ID, idade, nome, tipo, raca);
            clientes.get(retornoIndexClient(idDono)).insertAnimal(cat);
        }
    }

    public ArrayList<Cliente> getClientes() {
        return clientes;
    }

    public void setClientes(ArrayList<Cliente> clientes) {
        this.clientes = clientes;
    }

    public ArrayList<Veterinario> getVeterinarios() {
        return veterinarios;
    }

    public void setVeterinarios(ArrayList<Veterinario> veterinarios) {
        this.veterinarios = veterinarios;
    }
    
    
    
}
