package javaapplication7;

import java.util.Scanner;

public class Main {

    public static Fatura setFatura(String identificador, String descricao, int quantidade,double preco)
    {
        Fatura f = new Fatura();

        f.setIdentificador(identificador);
        f.setDescricao(descricao);
        f.setQuantidade(quantidade);
        f.setPreco(preco);

        return f;
    }

    public static void retorno(Fatura f)
    {
        System.out.println("=================================");
        System.out.printf("Fatura: %s \n", f.getIdentificador());
        System.out.printf("Descrição: %s \n", f.getDescricao());
        System.out.printf("Quantidade: %d e Valor: R$ %f\n",f.getQuantidade(), f.getPreco());
        System.out.printf("Fatura Final: R$ %f\n", f.getInvoiceAmount());
        System.out.println("=================================");

    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Fatura fat = new Fatura();
        
        System.out.println("=================================");

        System.out.println("Digite o Identificador");
        String identificador = input.nextLine();

        System.out.println("Digite a Descricao");
        String descricao = input.nextLine();

        System.out.println("Digite a quantidade");
        int quantidade = Integer.parseInt(input.nextLine());

        System.out.println("Digite o valor");
        double preco = Double.parseDouble(input.nextLine());

        fat = setFatura(identificador, descricao, quantidade, preco);
        retorno(fat);

    }
    
}
