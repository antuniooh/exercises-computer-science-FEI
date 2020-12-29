package aula03ex1;

public class Funcionario {
    
    public Funcionario(){};
    
    public Funcionario(int idade, int numero, String nome, String sexo){
      this.idade = idade;
      this.numero = numero;
      this.nome = nome;
      this.sexo = sexo;
    }
    
    public Funcionario(String nome, int numero, int idade, String sexo){
      this.idade = idade;
      this.numero = numero;
      this.nome = nome;
      this.sexo = sexo;
    }
    
    public String getNome(){
      return nome;
    }
    
    public int getIdade(){
      return idade;
    }
    
    private int idade = 30;
    private int numero;
    private String nome;
    private String sexo;
}
