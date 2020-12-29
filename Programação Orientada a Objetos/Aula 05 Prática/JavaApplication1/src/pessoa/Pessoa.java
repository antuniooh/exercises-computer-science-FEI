/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pessoa;

/**Classe para objetos do tipo Pessoa, onde serão contidos, valores e métodos para o mesmo.
* @author unifansilva
*/
public class Pessoa {
    protected String nome;
    protected String sobrenome;
    protected int idade;

     /** Método construtor do objeto do tipo pessoa**/    
    public Pessoa(String nome, String sobrenome, int idade) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.idade = idade;
    }
     /** Método construtor vazio do objeto do tipo pessoa**/    
    public Pessoa() {
    }
    
    
/** Método para retorno do nome da pessoa
 * @return String - Nome da pessoa */
    public String getNome() {
        return nome;
    }

    /** Método para retorno do sobrenome da pessoa
 * @return String - Sobrenome da pessoa */
    public String getSobrenome() {
        return sobrenome;
    }

    /** Método para retorno da idade da pessoa
 * @return Int - Idade da pessoa */
    public int getIdade() {
        return idade;
    }
    
    
    
    
}
