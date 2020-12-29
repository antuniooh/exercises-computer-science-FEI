/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex02;
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

        lista2.add("Green");
        lista2.add("Blue");
        lista2.add("Yellow");

        int soma = 0;
        for(String i : lista1)
        {
            for(String j: lista2)
            {
                if(i == null ? j == null : i.equals(j))
                    soma++;
            }
        }

        if(lista1.size() == soma)
            System.out.println("BOA");
        else
            System.out.println("IXI");
    }
}
