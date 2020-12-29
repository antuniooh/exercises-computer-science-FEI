
package Ex03;

public class Main {
    
    public static void main(String[] args) {
        
        // agregação - todos criados no main
        // afeta outras classes, mesmo com o vinculo + fraco
        Aluno aluno = new Aluno();
        Disciplina disciplina = new Disciplina();
        Professor professor = new Professor();
        
        professor.setNome("Danilo");
        professor.setDepartamento("Computação");
        
        disciplina.setCodigo("666111");
        disciplina.setNome("POO");
        
        aluno.setNome("Julion");
        aluno.setRA("22.119.001-0");
        aluno.setCurso(disciplina.getNome());
         
        System.out.println(aluno.getCurso());
        
        
    }
}
