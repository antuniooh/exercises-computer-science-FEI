/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex03;

/**
 *
 * @author antonio
 */
public class Tela implements Output{

    public Tela() {        
    }

    @Override
    public void print(String text) {
        System.out.println(text);
    }
    
    
}
