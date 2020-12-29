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
public class Factory {
    public Output getOutput(int num){
        if(num == 0)
            return new File();
        else
            return new Tela();
    }

    public Factory() {
    }
    
}
