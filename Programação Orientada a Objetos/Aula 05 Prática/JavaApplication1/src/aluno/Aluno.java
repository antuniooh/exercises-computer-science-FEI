/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aluno;
import pessoa.Pessoa;

/**Classe para objetos do tipo Aluno, onde serão contidos, valores e métodos para o mesmo.
* @author unifansilva
*/
public class Aluno extends Pessoa{
    private String curso;

    /** Método construtor do objeto do tipo aluno com atributos herdados**/    
    public Aluno(String nome, String sobrenome, int idade, String curso) {
        super(nome, sobrenome, idade);
        this.curso = curso;
    }
    
    /** Método construtor vazio do objeto do tipo aluno com atributos herdados**/    
    public Aluno() {
    }
  

    /** Método para retorno do curso do aluno
 * @return String - Curso do aluno*/
    public String getCurso() {
        return curso;
    }
    
    /** Método para atribuir nome do curso ao atributo da classe aluno
      * @param curso - Novo nome do curso
     */
    public void setCurso(String curso) {
        this.curso = curso;
    }
    
     /**Método para retorno dos valores atribuidos ao objeto Aluno */
    public void print()
    {
        System.out.println("==========================");
        System.out.println("Nome: " + this.getNome());
        System.out.println("Sobrenome: " + this.getSobrenome());
        System.out.println("Idade: " + this.getIdade());
        System.out.println("Curso: " + this.getCurso());
        System.out.println("==========================");
    }
    
    
    
    

  


}
