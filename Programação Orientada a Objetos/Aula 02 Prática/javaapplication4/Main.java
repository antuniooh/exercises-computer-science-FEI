package javaapplication4;

import java.util.Scanner;

public class Main {

    public static Televisao setTelevisao(String modelo, float preco, float tamanho,int volume,
    int canal, boolean ligada)
    {
        Televisao tv = new Televisao();

        tv.setModelo(modelo);
        tv.setPreco(preco);
        tv.setTamanho(tamanho);
        tv.setVolume(volume);
        tv.setCanal(canal);
        tv.setLigada(ligada);

        return tv;
    }

    public static void retorno(Televisao tv)
    {
        System.out.println("=================================");
        System.out.println("ESTADO DA TELEVISÃO\n");
        System.out.printf("Modelo: %s \n", tv.getModelo());
        System.out.printf("Preço: R$ %f e Tamanho: %f cm\n", tv.getPreco(), tv.getTamanho());
        System.out.printf("Volume Atual: %d\n ", tv.getVolume());
        System.out.printf("Canal Atual: %d\n ", tv.getCanal());
        System.out.printf("Ligada? %b%n\n ", tv.isLigada());
        System.out.println("=================================");
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Televisao tv1 = new Televisao();
        Televisao tv2 = new Televisao();

        for(int i = 1; i < 3; i++){
            System.out.println("=================================");

            System.out.printf("Digite o Modelo da Televisão %d: ", i);
            String modelo =  input.nextLine();

            System.out.printf("Digite o Preço da Televisão %d: ", i);
            float preco =  Float.parseFloat(input.nextLine());
            
            System.out.printf("Digite o Tamanho da Televisão %d: ", i);
            float tamanho =  Float.parseFloat(input.nextLine());

            System.out.printf("Digite o Volume Atual da Televisão %d: ", i);
            int volume =  Integer.parseInt(input.nextLine());

            System.out.printf("Digite o Canal Atual da Televisão %d: ", i);
            int canal =  Integer.parseInt(input.nextLine());

            System.out.printf("A Televisão %d: está ligada: ", i);
            boolean ligada =  Boolean.parseBoolean(input.nextLine());

            switch (i) {
                case 1:
                    tv1 = setTelevisao(modelo, preco, tamanho, volume, canal, ligada);
                    break;
                case 2:
                    tv2 = setTelevisao(modelo, preco, tamanho, volume, canal, ligada);
                    break;
            }
        }

        System.out.println("Volume da Televisão 1 alterado:");
        tv1.alteraVolume(10);
        retorno(tv1);
        System.out.println("Volume da Televisão 1 alterado:");
        tv1.alteraVolume(-5);
        retorno(tv1);

        System.out.println("Volume da Televisão 2 alterado:");
        tv2.alteraVolume(10);
        retorno(tv2);
        System.out.println("Volume da Televisão 2 alterado:");
        tv2.alteraVolume(-5);
        retorno(tv2);

        System.out.println("Estado da Televisão 2 alterado:");
        tv2.setLigada(false);
        retorno(tv2);
        System.out.println("Volume da Televisão 2 alterado:");
        tv2.alteraVolume(-5);
        retorno(tv2);
    }
    
}
