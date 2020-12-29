package javaapplication5;

public class Data {
    
    //atributes 
    private int dia;
    private int mes;
    private int ano;
    
    public Data(){
        
    }
    public void setDia(int dia) {
        if(dia > 0 && dia <=31)
        {
            this.dia = dia;
        }
        else
        {
            System.out.println("=========================================");
            System.out.println("Dia inválido, valor definido como 1...");
            dia = 1;
        }
    }   

    public void setMes(int mes) {
        if(mes > 0 && mes <= 12)
        {
            this.mes = mes;
        }
        else
        {
            System.out.println("=========================================");
            System.out.println("Mês inválido, valor definido como 1...");
            mes = 1;
        }
    }

    public void setAno(int ano) {
        if(ano > 0)
        {
            this.ano = ano;
        }
        else
        {
            System.out.println("=========================================");
            System.out.println("Ano inválido, valor definido como 2000...");
            ano = 2000;
        }
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

    public void exibeData()
    {
        System.out.println("=================================");
        System.out.printf("Data: %d/%d/%d \n", dia, mes, ano);
        System.out.println("=================================");
    }

    

}
