package Exercicio02;

public class Data {
    
    //atributes 
    private int dia;
    private int mes;
    private int ano;
    private boolean bissexto;
    private int[] diasMes = {31,diaFevereiro(),31,30,31,30,31,31,30,31,30,31};
    
    public Data(){
        
    }

    public Data(int mes, int dia, int ano)
    {
        setAno(ano);
        setMes(mes);
        setDia(dia);
    }

    public int diaFevereiro()
    {
        int dia = 0;
        if(bissexto = true) 
        {
            dia = 29;
        }
        else
        {
            dia = 28;
        }
        return dia;

    }

    public void mesValue(String mes)
    {
        switch(mes)
        {
            case "Janeiro":
                this.mes = 1;
                break;
            case "Fevereiro":
                this.mes = 2;
                break;
            case "Março":
                this.mes = 3;
                break;
            case "Abril":
                this.mes = 4;
                break;
            case "Maio":
                this.mes=5;
                break;
            case "Junho":
                this.mes = 6;
                break;
            case "Julho":
                this.mes = 7;
                break;
            case "Agosto":
                this.mes = 8;
                break;
            case "Setembro":
                this.mes = 9;
                break;
            case "Outubro":
                this.mes = 10;
                break;
            case "Novembro":
                this.mes = 11;
                break;
            case "Dezembro":
                this.mes = 12;  
                break;     
        }
    }

    public Data(String mes, int dia, int ano)
    {
        setDia(dia);
        setAno(ano);
        mesValue(mes);
    }
    
    public Data(int diaTotal, int ano)
    {
        setAno(ano);

        int soma = 0;
        int i;
        for(i = 0; soma < diaTotal; i++)
        {
            soma+= diasMes[i];
        }
        this.mes = (i);
        int diaReal = diaTotal - totalDia(mes);
        setMes(mes);
        setDia(diaReal);
    }

    public int totalDia(int mes)
    {
        int soma= 0;
        int i;
        for(i =0; i < mes; i++)
        {
            soma+= diasMes[i];
        }
        return soma;
    }

    public String stringMes(int mes)
    {
        String mesText = "";

        switch(mes)
        {
            case 1:
                mesText = "Janeiro";
                break;
            case 2:
                mesText = "Fevereiro";
                break;
            case 3:
                mesText ="Março";
                break;
            case 4:
                mesText ="Abril";
                break;
            case 5:
                mesText = "Maio";
                break;
            case 6:
                mesText = "Junho";
                break;
            case 7:
                mesText = "Julho";
                break;
            case 8:
                mesText = "Agosto";
                break;
            case 9:
                mesText = "Setembro";
                break;
            case 10:
                mesText =  "Outubro";
                break;
            case 11:
                mesText = "Novembro";
                break;
            case 12:
                mesText = "Dezembro";   
                break;   
        }
        return mesText;
    }

    public void printAll()
    {
        System.out.println("=================================");
        System.out.printf("I. %d/%d/%d: \n", this.mes,this.dia , this.ano);
        System.out.printf("II. %s %d,%d: \n", stringMes(this.mes), this.dia, this.ano);
        System.out.printf("III. %d %d: \n",totalDia(this.mes-1) + this.dia, this.ano);
    }

    public void setDia(int dia) {
        if(dia > 0 && dia <= 31)
        {
            this.dia = dia;
        }
        else
        {
            this.dia = 1;
        }
    }   

    public void setMes(int mes) {
        if(mes > 0 && mes <= 12)
        {
            this.mes = mes;
        }
        else
        {
            this.mes = 1;
        }
    }

    public void setAno(int ano) {
        if(ano > 0)
        {
            this.ano = ano;
        }
        else
        {
            this.ano = 2000;
        }

        if(ano %4 == 0 && ano %100 !=0)
        {
            this.bissexto = true;
        }
        else
        {
            this.bissexto = false;
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
