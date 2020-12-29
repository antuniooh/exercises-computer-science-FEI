package javaapplication7;

public class Fatura {
    
    //atributes 
    private String identificador;
    private String descricao;
    private int quantidade;
    private double preco;

    public Fatura()
    {

    }

    public String getIdentificador() {
        return identificador;
    }

    public String getDescricao() {
        return descricao;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public double getPreco() {
        return preco;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void setQuantidade(int quantidade) {
        if(quantidade < 0)
        {
            this.quantidade = 0;
        }
        else
        {
            this.quantidade = quantidade;
        }
    }
    public void setPreco(double preco) {
        if(preco < 0)
        {
            this.preco = 0;
        }
        else
        {
            this.preco = preco;
        }
    }

    public double getInvoiceAmount()
    {
        double valorFinal = (quantidade * 1.0) * preco; 

        return valorFinal;
        
    }

}
