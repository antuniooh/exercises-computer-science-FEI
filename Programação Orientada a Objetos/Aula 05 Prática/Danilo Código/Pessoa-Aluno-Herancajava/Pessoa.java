class Pessoa{
    public Pessoa(){}
    public Pessoa(String nome, String sobrenome, int idade){
        this.nome = nome; this.sobrenome = sobrenome; 
        this.idade = idade;    
    }
    public String getNome(){
        return nome;
    }      
    public String getSobreNome(){
        return sobrenome;
    }
    public int getIdade(){
        return idade;
    }
    
    protected String nome;
    protected String sobrenome;
    protected int idade;
};