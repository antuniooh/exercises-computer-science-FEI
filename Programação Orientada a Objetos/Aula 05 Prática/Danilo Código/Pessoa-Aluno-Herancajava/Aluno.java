class Aluno extends Pessoa{
    public Aluno(){
    super();
    };
    public Aluno(String nome, String sobrenome, int idade, String curso){
        super(nome, sobrenome, idade);
        this.curso = curso;
    }
    public void setCurso(String curso){
        this.curso = curso;
    }
    public String getCurso(){
        return curso;
    }
    public void print(){
        System.out.printf("%s %s %d %s\n", getNome(), getSobreNome(), getIdade(), getCurso());
    }
    
    private String curso;
};