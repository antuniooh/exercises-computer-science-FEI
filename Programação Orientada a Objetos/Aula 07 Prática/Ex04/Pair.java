/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex04;

/**
 *
 * @author antonio
 */
public class Pair <F, S> {
    private F value1;
    private S value2;

    public Pair() {
    }

    public Pair(F value1, S value2) {
        this.value1 = value1;
        this.value2 = value2;
    }

    public F getValue1() {
        return value1;
    }

    public void setValue1(F value1) {
        this.value1 = value1;
    }

    public S getValue2() {
        return value2;
    }

    public void setValue2(S value2) {
        this.value2 = value2;
    }
    
    
    
}
