/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ponto;

/**Classe para objetos do tipo Pessoa, onde serão contidos, valores e métodos para o mesmo.
* @author unifansilva
*/
public class Ponto {
    protected int x;
    protected int y;

    /** Método construtor do objeto do tipo ponto**/   
    public Ponto(int x, int y) {
        this.x = x;
        this.y = y;
    }
    /** Método construtor vazio do objeto do tipo ponto**/   
    public Ponto() {
    }
    
    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }
    
    
    
    

}
