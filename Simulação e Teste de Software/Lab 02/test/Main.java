//JFrame classe responsável por exibir a janela
package test;

import test.Ex2;

//Main - Nome da classe
public class Main {
    // Comando principal para execução do programa
    public static void main(String[] args) {
        // Criação de um objeto ex da classe Ex2
        Ex2 ex = new Ex2();
        // posição da tela ao abri-la
        ex.setLocation(400, 200);
        // tornando a tela visível
        ex.setVisible(true);
    }
}