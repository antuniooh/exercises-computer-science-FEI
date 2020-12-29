package javaapplication6;

public class Funcionario {
    
    //atributes 
    private String sobrenome;
    private String name;
    private double salario;

    public Funcionario(){
        
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSalario(double salario) {
        if(salario < 0)
        {
            this.salario = 0;
        }
        else
        {
            this.salario = salario;
        }
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public String getName() {
        return name;
    }

    public double getSalario() {
        return salario;
    }

    public double salarioAnual()
    {
        return (salario*12);
    }
    
    public void aumento(double porcentagem)
    {
        double newSalario = this.salario + this.salario*(porcentagem/100);
        setSalario(newSalario);
    }


}
