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
public class Singleton {
    private static Factory objetoUnico;
    
    private Singleton() {
    }
    
    public static Factory getInstance() {
        if (objetoUnico == null)
          objetoUnico = new Factory();
        return objetoUnico;
    }
}
