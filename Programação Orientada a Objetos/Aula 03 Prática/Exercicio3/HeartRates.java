package Exercicio3;

public class HeartRates {


    //atributes 
    private String sobrenome;
    private String name;
    private int dia;
    private int mes;
    private int ano;
    private int idade;
    private int frequenciaCardiacaMaxima;
    private double frequenciaCardiacaAlvoMin;
    private double frequenciaCardiacaAlvoMax;

    public HeartRates(String sobrenome, String name, int dia, int mes, int ano) {
        this.sobrenome = sobrenome;
        this.name = name;
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public double getFrequenciaCardiacaAlvoMin() {
        return frequenciaCardiacaAlvoMin;
    }

    public double getFrequenciaCardiacaAlvoMax() {
        return frequenciaCardiacaAlvoMax;
    }

    public void setFrequenciaCardiacaAlvoMin() {
        this.frequenciaCardiacaAlvoMin = getFrequenciaCardiacaMaxima() * 0.5;
    }

    public void setFrequenciaCardiacaAlvoMax() {
        this.frequenciaCardiacaAlvoMax = getFrequenciaCardiacaMaxima() * 0.85;
    }

    public int getFrequenciaCardiacaMaxima() {
        return frequenciaCardiacaMaxima;
    }

    public void setFrequenciaCardiacaMaxima() {
        this.frequenciaCardiacaMaxima = 220 - getIdade();
    }
   

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public String getName() {
        return name;
    }

    public int getDia() {
        return dia;
    }

    public int getMes() {
        return mes;
    }

    public int getAno() {
        return ano;
    }

    public HeartRates(){};

    public int getIdade() {
        return idade;
    }

    public void setIdade() {
          
     if(this.mes < 3){
         this.idade = 2020 - this.ano;
     }
     else
     {
         this.idade = 2019 - this.ano;
     }
    }
   
}