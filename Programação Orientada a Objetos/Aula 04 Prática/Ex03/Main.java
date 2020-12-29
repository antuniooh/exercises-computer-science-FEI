/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex03;
import java.util.ArrayList;

/**
 *
 * @author unifansilva
 */
public class Main {
    public static void main(String[] args) {
        ArrayList<String> lista1 = new ArrayList<>();
        ArrayList<String> lista2 = new ArrayList<>();

        lista1.add("Blue");
        lista1.add("Red");
        lista1.add("Green");

        for(String i : lista1)
        {
            lista2.add(i);
        }

        for(String j: lista2)
            System.out.println(j + "\n");
    }
}
