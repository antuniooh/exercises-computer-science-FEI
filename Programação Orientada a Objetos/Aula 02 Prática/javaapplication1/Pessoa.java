package javaapplication1;

public class Pessoa {
    
    //atributes 
    private String cpf;
    private String name;
    private int idade;

    public Pessoa(){
        
    }

    public Pessoa(String cpf, String name, int idade)
    {
        this.cpf = cpf;
        this.name = name;
        this.idade = idade;
    }

    public String getCpf()
    {
        return this.cpf;
    }
    public void setCpf(String newCpf)
    {
        this.cpf = newCpf;
    }

    public String getName()
    {
        return this.name;
    }
    public void setName(String newName)
    {
        this.name = newName;
    }

    public int getIdade()
    {
        return this.idade;
    }
    public void setIdade(int newIdade)
    {
        this.idade = newIdade;
    }


}
