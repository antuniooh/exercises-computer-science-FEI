/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex03;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 *
 * @author antonio
 */
public class File implements Output {


    public File() {

    }

    @Override
    public void print(String text) {
        try {
            FileWriter arquivo = new FileWriter("output.txt");
            PrintWriter writeFile = new PrintWriter(arquivo);

            writeFile.println(text);
            
            arquivo.close();
        } catch (IOException e) {
        }
    }

}
