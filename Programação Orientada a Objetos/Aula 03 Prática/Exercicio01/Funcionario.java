package Exercicio01;

public class Funcionario {
    
    //atributes 
    private String sobrenome;
    private String name;
    private double salario;
    private int idade;
    private String sexo;
    private int numero;

    public Funcionario(){};
    public Funcionario(String name, String sobrenome,double  salario, int idade, String sexo, int numero)
    {
        setName(name);
        setSobrenome(sobrenome);
        setSalario(salario);
        setIdade(idade);
        setSexo(sexo);
        setNumero(numero);
    }

    public void setSobrenome(final String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public void setName(final String name) {
        this.name = name;
    }

    public void setSalario(final double salario) {
        if (salario < 0) {
            this.salario = 0;
        } else {
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

    public void setIdade(final int idade) {
        this.idade = idade;
    }

    public void setSexo(final String sexo) {
        this.sexo = sexo;
    }

    public void setNumero(final int numero) {
        this.numero = numero;
    }

    public String getSexo() {
        return sexo;
    }

    public int getIdade() {
        return idade;
    }

    public int getNumero() {
        return numero;
    }

    public double salarioAnual() {
        return (salario * 12);
    }

    public void aumento(final double porcentagem)
    {
        final double newSalario = this.salario + this.salario*(porcentagem/100);
        setSalario(newSalario);
    }

}
