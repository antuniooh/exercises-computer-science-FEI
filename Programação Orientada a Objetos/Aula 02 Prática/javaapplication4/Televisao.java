package javaapplication4;

public class Televisao {
    
    //atributes 
    private String modelo;
    private float preco;
    private float tamanho;
    private int volume;
    private int canal;
    private boolean ligada;

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }

    public void setTamanho(float tamanho) {
        this.tamanho = tamanho;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public void setCanal(int canal) {
        this.canal = canal;
    }

    public void setLigada(boolean ligada) {
        this.ligada = ligada;
    }

    public String getModelo() {
        return modelo;
    }

    public float getPreco() {
        return preco;
    }

    public float getTamanho() {
        return tamanho;
    }

    public int getVolume() {
        return volume;
    }

    public int getCanal() {
        return canal;
    }

    public boolean isLigada() {
        return ligada;
    }

    public void alteraVolume(int newVolume)
    {
        if(ligada == true)
        {
            if(volume + newVolume < 0)
            {
                volume = 0;
            }
            else
            {
                volume += newVolume;
            }
        }
        else
        {
            System.out.println("=========================================");
            System.out.println("Televisão delsigada, não é possivel alterar");
        }
    }
    public void alteraCanal(int newCanal)
    {
        if(ligada == true)
        {
            if(canal + newCanal <= 0)
            {
                canal = 1;
            }
            else
            {
                canal += newCanal;
            }
        }
        else
        {
            System.out.println("=========================================");
            System.out.println("Televisão delsigada, não é possivel alterar");
        }
    }
    public Televisao(){
        
    }

    

}
